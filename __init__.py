# __init__.py
from .enhancer import enhance_image
from .config import ENHANCEMENT_FACTOR

def main(input_image_path, output_image_path):
    enhance_image(input_image_path, output_image_path, ENHANCEMENT_FACTOR)
