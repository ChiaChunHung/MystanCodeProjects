"""
File: color_channel_filter.py
Author: Chia-Chun Hung
--------------------------------------------------
This script demonstrates basic color channel filtering
using pixel-level manipulation on an image.

It isolates individual RGB channels by removing the other
two color components. Each result highlights the corresponding
red, green, or blue intensities of the original image.

These techniques are foundational for understanding how color
channels interact and are commonly used in image preprocessing
and computer vision.
"""

from simpleimage import SimpleImage


def main():
    """
    Run your desired photoshop functions here.
    You should save the return value of the image and then
    call .show() to visualize the output of your program.
    """
    filepath = 'images/stanford.jpg'
    img = SimpleImage(filepath)
    img.show()
    new_img_red = red_channel(img)
    new_img_red.show()
    new_img_blue = blue_channel(img)
    new_img_blue.show()
    new_img_green = green_channel(img)
    new_img_green.show()


def red_channel(img):
    """
    remove all blue and green colors from the photo to enhance
    the red channel of its pixels (the R in RGB).
    ---------------------------------------------------
    :param img: SimpleImage, the original image
    :return: SimpleImage, the updated image with all pixels turning red
    """
    for pixel in img:
        pixel.green = 0
        pixel.blue = 0
    return img


def blue_channel(img):
    """
    Removes the red and green channels to enhance the blue channel
    of each pixel.
    ---------------------------------------------------
    :param img: SimpleImage, the original image
    :return: SimpleImage, the blue-highlighted image
    """
    for pixel in img:
        pixel.red = 0
        pixel.green = 0
    return img


def green_channel(img):
    """
    Removes the red and blue channels to enhance the green channel
    of each pixel.
    ---------------------------------------------------
    :param img: SimpleImage, the original image
    :return: SimpleImage, the green-highlighted image
    """
    for pixel in img:
        pixel.red = 0
        pixel.blue = 0
    return img


if __name__ == '__main__':
    main()
