"""
File: horizontal_reflection.py
Name: Chia-Chun, Hung
------------------------------------
This script creates a horizontally mirrored version of an image.
It constructs a new image that displays the original on the left
and its mirrored version on the right.

This demonstrates coordinate-based image transformation, a key
concept in computer vision and image manipulation.
"""


from simpleimage import SimpleImage


def main():
    """
    Loads an image, constructs a horizontally flipped composite
    by placing the original on the left and its mirror on the right.
    Displays both the original and final composite image.
    """
    img = SimpleImage("images/poppy.png")
    img.show()
    b_img = SimpleImage.blank(img.width*2, img.height)          # Create blank image twice as wide
    # b_img = img.blank(img.width*2, img.height)
    b_img.show()
    for x in range(img.width):
        for y in range(img.height):
            img_pixel = img.get_pixel(x, y)
            # Copy original pixel to the left half of the new image
            b_img_pixel1 = b_img.get_pixel(x, y)
            b_img_pixel1.red = img_pixel.red
            b_img_pixel1.blue = img_pixel.blue
            b_img_pixel1.green = img_pixel.green
            # Copy mirrored pixel to the right half of the new image
            b_img_pixel2 = b_img.get_pixel(b_img.width-1-x, y)
            b_img_pixel2.red = img_pixel.red
            b_img_pixel2.blue = img_pixel.blue
            b_img_pixel2.green = img_pixel.green
    b_img.show()


if __name__ == '__main__':
    main()
