import os
from utils.image_resizer import resize_image
from utils.file_handler import find_images, create_output_folder, build_output_path

def redim_image(input_path, required_width):
    images = find_images(input_path)
    output_path = create_output_folder(input_path)

if __name__=="__main__":
    input_path = None
    required_width = None
    redim_image(input_path, required_width)