"""
File: bouncing_ball.py
Name: chia-chun, Hung
-------------------------
Description:
This bouncing ball simulation was implemented as part of SC101 Assignment 1.
The assignment required simulating realistic physical behavior—gravity, bouncing,
and energy reduction—based on given constants and animation mechanics.

In this file, I completed the main control flow and event-handling logic, including:
- Implementing the `drop_till_end()` function to simulate gravity and bouncing with energy loss.
- Managing user interaction logic through `dropping_process()` to restrict to three runs and avoid interruptions during animations.
- Integrating global variables and constants in a modular, readable way.
- Writing all explanatory docstrings and comments to clarify the animation logic for future reviewers.

This project deepened my understanding of Python control structures, GUI event handling,
and simulating real-world physics behavior through code.
"""

from campy.graphics.gobjects import GOval
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause
from campy.gui.events.mouse import onmouseclicked

# Constants
VX = 3
DELAY = 10
GRAVITY = 1
SIZE = 20
REDUCE = 0.9
START_X = 30
START_Y = 40

# Global Variables
window = GWindow(800, 500, title='bouncing_ball.py')
ball = GOval(20, 20)                               # Only one ball is used throughout, so it's declared globally.
switch = True                                      # Switch to prevent restarting the animation while a drop is ongoing.
how_many_lives = 3                                 # Number of allow ball drops (user interactions).


def main():
    """
    This program simulates a bouncing ball at
    (START_X, START_Y) that has VX as x velocity
    and 0 as y velocity. Each bounce reduces y
    velocity to REDUCE of itself.
    """
    ball.filled = True
    window.add(ball, x=START_X, y=START_Y)            # show the ball at its initial position before clicks.
    onmouseclicked(dropping_process)                  # start mouse listener to trigger ball drop on click.


def dropping_process(_):                              # underscore used, because mouse event is not needed
    """
    This function triages the conditions
    set off by the clicks of the mouse.
    """
    global switch                                    # Because this global flag is reassigned, declare global.
    global how_many_lives                            # Because this global count is reassigned, declare global.
    if switch:                                       # When flag is True, allow the ball drop animation to start.
        switch = False                               # Close the flag to prevent restarting the drop mid-animation.
        if how_many_lives > 0:                       # Check if user still has drops left.
            drop_till_end()                          # Run the drop animation.
            how_many_lives -= 1                      # Decrement remaining drops.
            switch = True                            # Reopen flag after animation ends to allow next drop.
        else:
            pass                                     # No drops left, do nothing.
    else:
        pass
        # Ignore clicks while the ball is already dropping or if no lives remain.


def drop_till_end():
    """
    This function simulates the motion trajectory of
    a ball dropping from a height and bouncing until it
    exits the window.
    """
    ball_v = 0                                        # Vertical velocity initialized to 0.
    while True:                                       # Keep moving the ball until it leaves the window.
        ball.move(VX, ball_v + GRAVITY)               # Move the ball diagonally down.
        ball_v += GRAVITY                             # Gravity increases vertical speed.
        pause(DELAY)

        if ball.y >= 500:                             # Ball hits the bottom, initiate bounce.
            ball.move(0, -(ball.y - 500))             # Correct position to exactly on the floor.
            bounce_back_v = -ball_v * REDUCE          # Bounce upward with reduced velocity.
            while True:                               # Move ball upward until it loses upward velocity.
                ball.move(VX, bounce_back_v)
                bounce_back_v += GRAVITY              # Gravity slows the upward movement.
                pause(DELAY)
                if bounce_back_v >= 0:                # Ball stop rising when upward speeds become negative
                    break                             # Exit upward movement loop to start falling again
            ball_v = 0                                # Reset vertical velocity for next fall
        if ball.x >= 800:                             # Ball has exited the window, end animation
            break
    window.add(ball, x=START_X, y=START_Y)            # Reset ball to starting position after it exits window.


if __name__ == "__main__":
    main()
