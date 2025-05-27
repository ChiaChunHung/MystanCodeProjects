"""
File: breakout,py
Name: Chia-Chun, Hung
---------------------------------------------------
Description:
Completed as part of SC101 Assignment 2. I implemented the main game loop logic including
ball movement, collision detection, and life tracking. I also integrated user interaction
handling and game state updates to coordinate with the graphics module.
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

FRAME_RATE = 10         # 100 frames per second
NUM_LIVES = 3			# Number of attempts


def main():
    # Initialize game objects and variables
    graphics = BreakoutGraphics()
    number_of_attempts = 0
    num_of_bricks = graphics.get_brick_num()
    number_of_brick_remove = 0

    # Main game loop
    while True:
        if graphics.switch:
            # Start ball movement when user clicks. Speed is set only once on first click.
            vx = graphics.get_vx()
            vy = graphics.get_vy()

            # ball animation loop
            while True:
                # update
                graphics.ball.move(vx, vy)
                # Check collision at ball's corners
                obj_checker = False
                while True:
                    may_be_obj = graphics.window.get_object_at(graphics.ball.x, graphics.ball.y)
                    if may_be_obj is not None:
                        obj_checker = True
                        break
                    may_be_obj = graphics.window.get_object_at(graphics.ball.x + graphics.ball_radius * 2,
                                                               graphics.ball.y)
                    if may_be_obj is not None:
                        obj_checker = True
                        break
                    may_be_obj = graphics.window.get_object_at(graphics.ball.x,
                                                               graphics.ball.y + graphics.ball_radius * 2)
                    if may_be_obj is not None:
                        obj_checker = True
                        break
                    may_be_obj = graphics.window.get_object_at(graphics.ball.x + graphics.ball_radius * 2,
                                                               graphics.ball.y + graphics.ball_radius * 2)
                    if may_be_obj is not None:
                        obj_checker = True
                        break
                    if not obj_checker:
                        break
                if obj_checker:
                    # Ball hit an object
                    if may_be_obj.y == graphics.paddle.y:
                        graphics.window.add(graphics.ball, x=graphics.ball.x, y=graphics.paddle.y-graphics.ball.height)
                        vy = -vy
                    else:
                        graphics.window.remove(may_be_obj)
                        number_of_brick_remove += 1
                        vy = -vy
                # Check wall collisions (left/right reverse vx; top/bottom reverse vy)
                if graphics.ball.x <= 0 or graphics.ball.x+graphics.ball.width >= graphics.window.width:
                    vx = -vx
                if graphics.ball.y <= 0:
                    vy = -vy
                if graphics.ball.y+graphics.ball.height >= graphics.window.height:
                    graphics.switch = False
                    graphics.window.add(graphics.ball, x=(graphics.window.width - graphics.ball.width)/2,
                                        y=(graphics.window.height - graphics.ball.height) / 2)
                    number_of_attempts += 1
                    # lose a life
                    break
                if number_of_brick_remove == num_of_bricks:
                    graphics.window.add(graphics.ball, x=(graphics.window.width - graphics.ball.width) / 2,
                                        y=(graphics.window.height - graphics.ball.height) / 2)
                    break
                # pause
                pause(FRAME_RATE)
        else:
            graphics.ball.move(0, 0)            # ball stays still if not started
        pause(FRAME_RATE)                       # control game refresh rate
        if number_of_attempts == NUM_LIVES:     # game over
            break
        if number_of_brick_remove == num_of_bricks:
            break


if __name__ == '__main__':
    main()
