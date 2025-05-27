"""
File: pixel_region_filters.py
Author: Chia-Chun Hung
--------------------------------------------------
This script implements several image processing filters that
apply transformations to specific pixel regions based on their
coordinates:

1. left_half_darken: darkens the left half of the image
2. upper_left_lower_right_darken_1: darkens upper-left and lower-right quadrants, brightens the others
3. upper_left_lower_right_darken_2: alternate logic for the same region-based effect
4. gray_scale: converts the entire image to grayscale

These effects demonstrate spatial-based pixel manipulation,
a foundational concept in image preprocessing and computer vision.
"""


from simpleimage import SimpleImage


def main():
    """
    Displays the original image and applies various pixel-level transformations:
    - Darkening the left half
    - Darkening opposite quadrants and brightening the rest
    - Grayscale conversion
    """
    img = SimpleImage('images/stop.png')
    img.show()

    # Darken the left half of the image
    left_half_darken_img = left_half_darken('images/stop.png')
    left_half_darken_img.show()

    # Darken upper-left and lower-right quadrants; brighten the others
    upper_left_lower_right_darken_img_1 = upper_left_lower_right_darken_1('images/stop.png')
    upper_left_lower_right_darken_img_1.show()
    upper_left_lower_right_darken_img_2 = upper_left_lower_right_darken_2('images/stop.png')
    upper_left_lower_right_darken_img_2.show()

    # Convert the image to grayscale
    gray_scale_img = gray_scale('images/stop.png')
    gray_scale_img.show()


# Darken the left half of the image by halving RGB values
def left_half_darken(filepath):
    """
    :param filepath: str, the file path of the original image (with respect to current directory)
    :return img: SimpleImage, the image with half horizontal area darken
    """
    img = SimpleImage(filepath)
    for x in range(img.width):
        for y in range(img.height):
            pixel = img.get_pixel(x, y)
            if x < img.width/2:
                pixel.red = pixel.red//2
                pixel.blue = pixel.blue//2
                pixel.green = pixel.green//2
    return img


# Darken upper-left and lower-right quadrants
# Brighten upper-right and lower-left quadrants
def upper_left_lower_right_darken_1(filepath):
    half_darken_img = SimpleImage(filepath)
    for x in range(half_darken_img.width):
        for y in range(half_darken_img.height):
            pixel = half_darken_img.get_pixel(x, y)
            if x < half_darken_img.width/2 and y < half_darken_img.height/2:
                pixel.red = pixel.red // 2
                pixel.blue = pixel.blue // 2
                pixel.green = pixel.green // 2
            elif x > half_darken_img.width/2 and y > half_darken_img.height/2:
                pixel.red = pixel.red // 2
                pixel.blue = pixel.blue // 2
                pixel.green = pixel.green // 2
            else:
                pixel.red *= 2
                pixel.green *= 2
                pixel.blue *= 2
    return half_darken_img


# Same region darkening/brightening as above with alternate logic
def upper_left_lower_right_darken_2(filepath):
    half_darken_img = SimpleImage(filepath)
    for x in range(half_darken_img.width):
        for y in range(half_darken_img.height):
            if x < half_darken_img.width/2:
                pixel = half_darken_img.get_pixel(x, y)
                if y < half_darken_img.height/2:
                    pixel.red = pixel.red//2
                    pixel.blue = pixel.blue//2
                    pixel.green = pixel.green//2
                else:
                    pixel.red *= 2
                    pixel.blue *= 2
                    pixel.green *= 2
            if x > half_darken_img.width/2:
                pixel = half_darken_img.get_pixel(x, y)
                if y > half_darken_img.height / 2:
                    pixel.red = pixel.red // 2
                    pixel.blue = pixel.blue // 2
                    pixel.green = pixel.green // 2
                else:
                    pixel.red *= 2
                    pixel.blue *= 2
                    pixel.green *= 2
    return half_darken_img


# Convert each pixel to grayscale by averaging RGB values
def gray_scale(filepath):
    """
    :param filepath: str, the file path of the original image (with respect to current directory)
    :return: SimpleImage, gray scaled image
    """
    gray_img = SimpleImage(filepath)
    for pixel in gray_img:
        avg = (pixel.red+pixel.blue+pixel.green)//3
        pixel.red = avg
        pixel.blue = avg
        pixel.green = avg
    return gray_img


if __name__ == '__main__':
    main()
