"""
File: green_screen_replacer.py
Author: Chia-Chun, Hung
--------------------------------------------------
This script performs green screen replacement by
compositing a subject image onto a new background.

It detects green-dominant pixels in the foreground image
and replaces them with the corresponding pixels from the
background image. This simulates a basic chroma key
replacement technique commonly used in photo and video editing.

This technique demonstrates color-based pixel classification
and is foundational in computer vision and image preprocessing.
"""


from simpleimage import SimpleImage


# Controls the threshold of detecting green screen pixel
THRESHOLD = 1.3

# Controls the upper bound for black pixel
BLACK_PIXEL = 120


def combine(bg, me):
    """
    Replaces green screen pixels in the foreground image with
    corresponding pixels from the background image.
    ---------------------------------------------------
    :param bg: SimpleImage, the background image
    :param me: SimpleImage, the foreground image with green screen
    :return: SimpleImage, the composite image with background inserted
    """
    for y in range(bg.height):
        for x in range(bg.width):
            pixel_me = me.get_pixel(x, y)
            avg = (pixel_me.red+pixel_me.blue+pixel_me.green) // 3
            total = pixel_me.red+pixel_me.blue+pixel_me.green
            if pixel_me.green > avg*THRESHOLD and total > BLACK_PIXEL:
                pixel_bg = bg.get_pixel(x, y)
                pixel_me.red = pixel_bg.red
                pixel_me.blue = pixel_bg.blue
                pixel_me.green = pixel_bg.green
    return me


def main():
    """
    Loads the green screen image and background image,
    resizes the background to match the subject image,
    and displays the final composite image.
    """
    fg = SimpleImage('images/jerry.jpeg')
    bg = SimpleImage('images/wave.jpeg')
    bg.make_as_big_as(fg)
    combined_img = combine(bg, fg)
    combined_img.show()


if __name__ == '__main__':
    main()
