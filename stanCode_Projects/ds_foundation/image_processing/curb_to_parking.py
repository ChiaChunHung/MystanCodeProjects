"""
File: curb_to_parking.py
Author: Chia-Chun Hung
--------------------------------------------------
This script processes an image to detect curb regions
by identifying red-dominant pixels. Once detected,
those pixels are converted to grayscale to visually
suggest that the curb can be treated as a valid parking space.

This demonstrates basic feature-based pixel classification
and image transformation, useful in computer vision and
data preprocessing tasks such as automated labeling or
region segmentation.
"""


from simpleimage import SimpleImage


THRESHOLD = 1.12


def main():
    """
    Loads an image, detects red-dominant curb pixels,
    and converts them to grayscale to indicate available parking space.
    """
    img = SimpleImage("images/curb.png")

    for pixel in img:                                 # loop through each pixel in the image
        avg = (pixel.red+pixel.green+pixel.blue)//3   # Calculate average brightness
        if pixel.red > avg * THRESHOLD:               # If red is significantly dominant, classify as curb
            # Convert the pixel to grayscale while preserving brightness
            pixel.red = avg
            pixel.blue = avg
            pixel.green = avg
    img.show()


if __name__ == '__main__':
    main()
