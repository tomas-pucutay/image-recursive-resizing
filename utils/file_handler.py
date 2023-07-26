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
    # Build output path based on original folder structure
    original_path = os.path.relpath(os.path.dirname(image_path), input_path)
    original_name = os.path.basename(image_path)
    new_path = os.path.join(output_path, original_path)
    image_output_path = os.path.join(new_path, original_name)

    # Create output folder if it doesn't exist
    os.makedirs(new_path, exist_ok=True)

    return image_output_path