import os
from PIL import Image

def resize_image(image_path, required_width):
    # Open image with Pillow
    image_pil = Image.open(image_path)
    return image_pil
