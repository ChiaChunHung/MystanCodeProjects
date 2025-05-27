"""
File: breakoutgraphics.py
Name: Chia-Chun, Hung
---------------------------------------------------
Description:
Completed as part of SC101 Assignment 2. I implemented the full graphical setup for the
Breakout game, including paddle, ball, brick layout, and mouse event handlers. This work
reinforced my understanding of class-based design and interactive game programming.

"""

from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

# Constants  (shared and configurable)
BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing
BRICK_WIDTH = 40       # Width of a brick (in pixels)
BRICK_HEIGHT = 15      # Height of a brick (in pixels)
BRICK_ROWS = 10        # Number of rows of bricks
BRICK_COLS = 10        # Number of columns of bricks
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels)
BALL_RADIUS = 10       # Radius of the ball (in pixels)
PADDLE_WIDTH = 75      # Width of the paddle (in pixels)
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels)
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels)
INITIAL_Y_SPEED = 7    # Initial vertical speed for the ball
MAX_X_SPEED = 5        # Maximum initial horizontal speed for the ball


class BreakoutGraphics:
    # Constructor
    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH, paddle_height=PADDLE_HEIGHT,
                 paddle_offset=PADDLE_OFFSET, brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS, brick_width=BRICK_WIDTH,
                 brick_height=BRICK_HEIGHT, brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING, title='Breakout'):

        # Create a graphical window, with some extra space
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)

        # Create a paddle
        self.paddle = GRect(paddle_width, paddle_height)
        self.paddle.filled = True
        self.window.add(self.paddle, x=(self.window.width-self.paddle.width)/2, y=(self.window.height-paddle_offset))

        # Center a filled ball in the graphical window
        self.ball = GOval(ball_radius*2, ball_radius*2)
        self.ball.filled = True
        self.window.add(self.ball, x=(self.window.width-self.ball.width)/2, y=(self.window.height-self.ball.height)/2)
        self.ball_radius = ball_radius

        # Default initial velocity for the ball
        self.__dx = 0
        self.__dy = 0

        # Initialize our mouse listeners
        onmousemoved(self.animate_of_paddle)                                      # make paddle move with user's mouse
        onmouseclicked(self.game_start_ball_drop)                                 # once user click, ball moves
        self.switch = False                                                       # before user click, ball stop

        # Draw bricks
        self.brick_rows = brick_rows
        self.brick_cols = brick_cols
        self.brick_offset = brick_offset
        self.brick_spacing = brick_spacing
        self.brick_width = brick_width
        self.brick_height = brick_height
        self.draw_bricks()                                                       # create all bricks

    def draw_bricks(self):
        brick_construction_x = 0                                                 # variable storing brick's x position
        brick_construction_y = self.brick_offset                                 # variable storing brick's y position
        for i in range(self.brick_rows):
            for j in range(self.brick_cols):
                brick = GRect(self.brick_width, self.brick_height)
                self.brick_color_painting(i, brick)
                self.window.add(brick, x=brick_construction_x, y=brick_construction_y)
                brick_construction_x += (self.brick_width + self.brick_spacing)
            brick_construction_x = 0                                             # rest brick's x position at each row
            brick_construction_y += (self.brick_height + self.brick_spacing)

    @staticmethod
    def brick_color_painting(i, brick):
        brick.filled = True
        if i <= 1:
            brick.fill_color = 'red'
            brick.color = 'red'
        elif i <= 3:
            brick.fill_color = 'gold'
            brick.color = 'gold'
        elif i <= 5:
            brick.fill_color = 'yellow'
            brick.color = 'yellow'
        elif i <= 7:
            brick.fill_color = 'green'
            brick.color = 'green'
        else:
            brick.fill_color = 'blue'
            brick.color = 'blue'

    def animate_of_paddle(self, mouse):
        """
        Whenever the mouse moves, the center of the paddle should follow the mouse.
        If the paddle reaches the boundary, it should not go beyond the edge
        """
        if mouse.x-self.paddle.width/2 <= 0:
            self.window.add(self.paddle, x=0, y=self.paddle.y)
        elif mouse.x+self.paddle.width/2 >= self.window.width:
            self.window.add(self.paddle, x=self.window.width-self.paddle.width, y=self.paddle.y)
        else:
            self.window.add(self.paddle, x=mouse.x-(self.paddle.width/2), y=self.paddle.y)

    def game_start_ball_drop(self, mouse):
        self.switch = True
        self.__dy = INITIAL_Y_SPEED
        self.__dx = random.randint(1, MAX_X_SPEED)
        if random.random() > 0.5:
            self.__dx = -self.__dx

    # return initial ball speed
    def get_vx(self):
        return self.__dx

    def get_vy(self):
        return self.__dy

    # return how many number of bricks
    def get_brick_num(self):
        return BRICK_COLS*BRICK_ROWS












