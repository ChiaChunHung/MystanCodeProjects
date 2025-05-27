"""
File: draw_line.py
Name: Chia-Chun Hung
------------------------------------------------------------------------------
Description:
Completed as part of SC101 Assignment 1. I implemented the core logic for distinguishing
odd/even mouse clicks to draw circles and lines, and managed user click tracking with
global variables. This task helped strengthen my understanding of event handling and
graphical programming using campy.
"""

from campy.graphics.gobjects import GOval, GLine
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked

# Constant controls the radius of the circle
SIZE = 5

# Global variables
window = GWindow()  # create a canvas window
times_of_click = 0  # count mouse clicks to determine odd/even
odd_clicks_x = 0    # store x coordinate of the first odd click
odd_clicks_y = 0    # store y coordinate of the first off click


def main():
    """
    This program creates lines on an instance of GWindow class.
    There is a circle indicating the user’s first click. A line appears
    at the condition where the circle disappears as the user clicks
    on the canvas for the second time.
    """
    onmouseclicked(drawing_process)


def drawing_process(mouse):
    """
    This function defines the actions that the computer
    should undertake every time the user clicked the mouse.
    """
    global times_of_click                                       # use the global variable so that it can be updated
    times_of_click += 1                                         # Increment click count on each mouse click
    if times_of_click % 2 != 0:                                 # odd-numbered click
        draw_a_circle(mouse.x, mouse.y)                         # draw a circle at the click location
    else:                                                       # even-numbered click
        draw_a_line(mouse.x, mouse.y)                           # draw a line and remove the previous circle


def draw_a_circle(mouse_x, mouse_y):
    """
    :param: mouse_x, int, x coordinate of user's mouse
    :param: mouse_y, int, y coordinate of user's mouse
    """
    global odd_clicks_x
    global odd_clicks_y
    oval = GOval(SIZE*2, SIZE*2)
    window.add(oval, x=mouse_x-SIZE, y=mouse_y-SIZE)
    odd_clicks_x = mouse_x                                      # record the x coordinate of the odd click
    odd_clicks_y = mouse_y                                      # record the y coordinate of the odd click


def draw_a_line(mouse_x, mouse_y):
    """
    :param: mouse_x, int, x coordinate of user's mouse
    :param: mouse_y, int, y coordinate of user's mouse
    """
    line = GLine(odd_clicks_x, odd_clicks_y, mouse_x, mouse_y)
    window.add(line)
    odd_clicks_circle = window.get_object_at(odd_clicks_x-SIZE/2, odd_clicks_y-SIZE/2)
    # Retrieve the circle object near the center of the previous (odd) click
    # The offset ensures we select the circle without accidentally selecting the line
    window.remove(odd_clicks_circle)


if __name__ == "__main__":
    main()
