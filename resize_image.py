# pip install Pillow

from PIL import Image

def resize_image(input_path, output_path, size):
    """
    Resize the image to the given size.

    Parameters:
    input_path (str): The path to the input image.
    output_path (str): The path to save the resized image.
    size (tuple): The desired size as a tuple (width, height).
    """
    with Image.open(input_path) as img:
        img = img.resize(size, Image.LANCZOS)  # Resize the image with LANCZOS filter
        img.save(output_path)  # Save the resized image

# Example usage:
input_image_path = 'path/to/your/input/image.jpg'
output_image_path = 'path/to/your/output/image.jpg'
desired_size = (800, 600)  # Width, Height

resize_image(input_image_path, output_image_path, desired_size)