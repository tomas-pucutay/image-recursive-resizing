import os
import glob

def find_images(input_path):
    # Recursively search all images in input folder
    images = glob.glob(os.path.join(input_path, '**', '*.jp*g'), recursive=True)
    return images

def create_output_folder(input_path):
    # Create output folder
    output_path = input_path + '_redim'
    os.makedirs(output_path, exist_ok=True)
    return output_path

def build_output_path(image_path, input_path, output_path):
    image_output_path = None
    return image_output_path