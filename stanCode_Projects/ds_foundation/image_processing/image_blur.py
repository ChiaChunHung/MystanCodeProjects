"""
File: image_blur.py
Name: Chia-Chun Hung
--------------------------------------------------
This script applies a box blur (mean filter) to an image by
averaging the RGB values of each pixel with its valid neighbors.

The blur is applied multiple times to increase the smoothing effect.
This basic image processing technique is useful for noise reduction
and is commonly used in data preprocessing for computer vision tasks.

"""

from simpleimage import SimpleImage


def blur(img):
    """
    Applies a single round of box blur to the input image.
    For each pixel, the new RGB value is calculated by averaging the values
    of that pixel and its neighboring pixels within a 3x3 grid, considering
    boundary conditions.
    ----------------------------------------------------------------------
    :param img: SimpleImage, the original image
    :return: SimpleImage, the blurred version of the image
    """
    b_img = SimpleImage.blank(img.width, img.height)
    for x in range(img.width):
        for y in range(img.height):
            r_sum = 0                                                          # Sum of red values in 3*3 neighborhood
            b_sum = 0                                                          # Sum of blue values in 3*3 neighborhood
            g_sum = 0                                                          # Sum of green values in 3*3 neighborhood
            count = 0                                                          # Count of valid pixels in neighborhood
            for i in range(-1, 2, 1):
                for j in range(-1, 2, 1):
                    if 0 <= x+i < img.width and 0 <= y+j < img.height:
                        pixel = img.get_pixel(x+i, y+j)
                        r_sum += pixel.red
                        b_sum += pixel.blue
                        g_sum += pixel.green
                        count += 1
            b_pixel = b_img.get_pixel(x, y)

            b_pixel.red = r_sum // count

            b_pixel.blue = b_sum // count

            b_pixel.green = g_sum // count

    return b_img


def main():
    """
    Loads an image, displays it, and applies the blur filter multiple
    times to amplify the smoothing effect. The final result is then shown.
    """
    old_img = SimpleImage("images/smiley-face.png")
    old_img.show()
    blurred_img = blur(old_img)
    for i in range(5):
        blurred_img = blur(blurred_img)
    blurred_img.show()


if __name__ == '__main__':
    main()
