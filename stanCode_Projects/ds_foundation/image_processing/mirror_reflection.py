"""
File: mirror_reflection.py
Author: Chia-Chun Hung
--------------------------------------------------
This script creates a visual lake reflection effect by vertically
mirroring an input image. The top half remains unchanged, while
the bottom half is a flipped copy of the top.

This demonstrates coordinate-based image transformation, a
fundamental technique in computer vision and digital image processing.
"""
from simpleimage import SimpleImage


def reflect(filename):
    """
    Generates a new image that mirrors the input image vertically.
    The original image is placed on the top, and the mirrored version
    is placed on the bottom.

    :param filename: str, the file path of the input image
    :return: SimpleImage, a vertically mirrored image
    """
    img = SimpleImage(filename)
    b_img = SimpleImage.blank(img.width, img.height*2)
    for x in range(img.width):
        for y in range(img.height):
            img_pixel = img.get_pixel(x, y)

            # Copy original pixel to upper half
            b_pixel_upper = b_img.get_pixel(x, y)
            b_pixel_upper.red = img_pixel.red
            b_pixel_upper.blue = img_pixel.blue
            b_pixel_upper.green = img_pixel.green

            # Copy same pixel to mirrored lower half
            b_pixel_lower = b_img.get_pixel(x, b_img.height-1-y)
            b_pixel_lower.red = img_pixel.red
            b_pixel_lower.blue = img_pixel.blue
            b_pixel_lower.green = img_pixel.green
    return b_img


def main():
    """
    Displays the original image and a vertically mirrored version
    to simulate a lake reflection effect.
    """
    original_mt = SimpleImage('images/mt-rainier.jpg')
    original_mt.show()
    reflected = reflect('images/mt-rainier.jpg')
    reflected.show()


if __name__ == '__main__':
    main()
