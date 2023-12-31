import os
from PIL import Image

def resize_image(image_path, required_width):
    try:
        # Open image with Pillow
        image_pil = Image.open(image_path)

        # Resize image to desired width and keep aspect ratio
        width, height = image_pil.size
        if width > required_width:
            proportion = required_width / width
            required_height = int(height * proportion)
            resized_image = image_pil.resize((required_width, required_height), Image.LANCZOS)
        else:
            resized_image = image_pil

        # Remove image metadata
        image_info = resized_image.info.copy()
        image_info.pop("exif", None)

        return resized_image, image_info
    
    except (OSError, IOError, Image.UnidentifiedImageError):
        # Return None if image cannot be identified
        return None, None
