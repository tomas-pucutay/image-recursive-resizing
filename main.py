import os
from utils.image_resizer import resize_image
from utils.file_handler import find_images, create_output_folder, build_output_path

def redim_image(input_path, required_width):
    images = find_images(input_path)
    output_path = create_output_folder(input_path)

    for image in images:
        try:
            image_output_path = build_output_path(image, input_path, output_path)

            # Resize image and get image_info
            resized_image, image_info = resize_image(image, required_width)

            if resized_image is not None:
                # Compress and save the resized image without the metadata
                resized_image.save(image_output_path, optimize=True, quality=85, **image_info)
                print(f'done {resized_image}')
        
        except Exception as e:
            # Skip images that cannot be processed
            print(f"Error processing image: {image}")
            print(e)
            continue

# Input folder path and output folder
if __name__=="__main__":
    input_path = os.path.join(os.getcwd(), 'images')
    required_width = 1200
    redim_image(input_path, required_width)