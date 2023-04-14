import openai
from PIL import Image
import requests

openai.api_key = "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"

def generate_cat_image():
    response = openai.Image.create(
        prompt="a cat",
        size="512x512",
        response_format="url"
    )
    image_url = response['data'][0]['url']
    image = Image.open(requests.get(image_url, stream=True).raw)
    return image
