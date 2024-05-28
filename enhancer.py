# enhancer.py
from PIL import Image, ImageEnhance

def enhance_image(input_image_path, output_image_path, enhancement_factor):
    image = Image.open(input_image_path)
    enhancer = ImageEnhance.Contrast(image)
    enhanced_image = enhancer.enhance(enhancement_factor)
    enhanced_image.save(output_image_path)
