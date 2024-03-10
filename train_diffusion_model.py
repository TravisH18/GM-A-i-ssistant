from diffusers import pipelines, utils, DataCollatorForTextImageDiffusion
from datasets import load_dataset

# Define Model and Dataset Paths
model_name = "0xJustin/Dungeons-and-Diffusion"  # Replace with your desired model
dataset_path = "TravisHudson/DND-Monster-Diffusion"  # Replace with your dataset path

# Load dataset
dataset = load_dataset(dataset_path)

# Function to preprocess data
def preprocess_function(examples):
  images = [utils.load_image(f) for f in examples["file_name"]]
  prompts = examples["prompt"]
  return {"image": images, "prompt": prompts}

# Preprocess dataset
train_dataset = dataset["train"].map(preprocess_function, batched=True)

# Data Collator
data_collator = DataCollatorForTextImageDiffusion()

# Load pipeline
pipe = pipelines.TextImageDiffusionPipeline.from_pretrained(
    model_name,
    revision="fp16",  # Use fp16 for faster training (if compatible with GPU)
    data_collator=data_collator,
)

# Fine-tune the pipeline on the prepared dataset
pipe.train(train_dataset, epochs=10, output_dir="models")  # Adjust epochs as needed

# Save the fine-tuned model for future use
pipe.save_pretrained("TravisHudson/DND-Monster-Diffusion")
pipe.push_to_hub("TravisHudson/DND-Monster-Diffusion")
