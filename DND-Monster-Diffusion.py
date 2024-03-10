# from diffusers import AutoPipelineForText2Image
from diffusers import StableDiffusionPipeline
import torch
# import torch
# pipeline = AutoPipelineForText2Image.from_pretrained().to("cuda")
#pipeline = DiffusionPipeline.from_pretrained("0xJustin/Dungeons-and-Diffusion")
# https://huggingface.co/docs/diffusers/tutorials/basic_training

# prompt = "New monster description"
# image = pipeline(prompt, num_inference_steps=25).images[0]
# print(image)

# once training is done


pipeline = StableDiffusionPipeline.from_pretrained("path/to/saved_model", torch_dtype=torch.float16, use_safetensors=True).to("cuda")

prompt = "New monster description"
image = pipeline(prompt="yoda").images[0]
image.save("yoda-pokemon.png")