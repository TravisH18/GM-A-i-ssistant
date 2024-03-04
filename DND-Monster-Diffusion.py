# from diffusers import AutoPipelineForText2Image
from diffusers import DiffusionPipeline
# import torch
# pipeline = AutoPipelineForText2Image.from_pretrained().to("cuda")
pipeline = DiffusionPipeline.from_pretrained("0xJustin/Dungeons-and-Diffusion")
# https://huggingface.co/docs/diffusers/tutorials/basic_training

prompt = "New monster description"
image = pipeline(prompt, num_inference_steps=25).images[0]
print(image)