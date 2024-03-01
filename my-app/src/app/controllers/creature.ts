import { Context, Get, HttpResponseOK } from '@foal/core';
import { HfInference } from '@huggingface/inference';
const hf = new HfInference("HF_TOKEN");

export class ApiController {

  @Get('/')
  index(ctx: Context) {
    return new HttpResponseOK('Hello world!');
  }

  @Get('/newImage')
  generator(ctx: Context) {
    const model = "stabilityai/stable-diffusion-2";
    const prompt = "award winning high resolution photo of a giant tortoise";

    try {
        const {image} = await hf.textToImage({
            inputs: prompt,
            model: model,
            parameters: {
                negative_prompt: 'blurry'
            }
        });

        document.getElementById("imgBuffer").innerHTML = image;
  } catch (err) {
    alert("Hugging Face Image generation error" + err.message);
  }

}