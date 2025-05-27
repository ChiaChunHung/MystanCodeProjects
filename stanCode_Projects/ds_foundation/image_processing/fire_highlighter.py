"""
File: fire_highlighter.py
Author: Chia-Chun Hung
--------------------------------------------------
This script processes a satellite or aerial image to identify
and highlight potential fire regions.

It uses a simple RGB thresholding approach to classify pixels
with dominant red intensity as fire. Fire pixels are highlighted
in bright red, while non-fire regions are converted to grayscale.

This technique demonstrates basic feature-based pixel classification,
commonly used in image preprocessing for anomaly detection in
data science and computer vision.
"""

from simpleimage import SimpleImage


HURDLE_FACTOR = 1.05


def highlight_fires(filename):
    """
    Detects fire regions in an image based on red-channel dominance.
    :param filename: str, path to the image file to analyze
    :return: SimpleImage, with fire regions highlighted in red and
             non-fire areas converted to grayscale
    """
    highlight_fire_img = SimpleImage(filename)
    for pixel in highlight_fire_img:
        avg = (pixel.red + pixel.blue + pixel.green)//3             # Compute average brightness
        if pixel.red > avg*HURDLE_FACTOR:                           # highlight fire pixel in red
            pixel.red = 255
            pixel.green = 0
            pixel.blue = 0
        else:                                                       # Convert non-fire pixel to grayscale
            pixel.red = avg
            pixel.blue = avg
            pixel.green = avg
    return highlight_fire_img


def main():
    """
    Loads an image, shows the original, then processes and displays
    a version with fire regions highlighted.
    """
    original_fire = SimpleImage('images/greenland-fire.png')
    original_fire.show()
    highlighted_fire = highlight_fires('images/greenland-fire.png')
    highlighted_fire.show()


if __name__ == '__main__':
    main()
