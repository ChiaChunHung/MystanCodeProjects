"""
File: extension_breakout.py
Name: Chia-Chun, Hung
-----------------------------------------------------------------------------------------------
Description:
Completed as part of SC101 Assignment 2. I extended the basic Breakout game by implementing
interactive features such as falling trash, black holes, and dynamic animations. I also managed
scene transitions, life tracking, and level-based difficulty changes using class-based design.
"""

from campy.gui.events.timer import pause
from extensions_breakoutgraphics import BreakoutGraphics
from campy.graphics.gobjects import GOval, GRect, GLabel, GPolygon
import random

FRAME_RATE = 10         # 100 frames per second
NUM_LIVES = 3			# Number of attempts
trash_switch = True


def main():
    """
    Initializes the game window, displays the opening animation, and handles the main game loop.
    Controls game flow including ball movement, object interactions, scoring, and life tracking.
    Includes multiple conditional triggers for events like falling trash and black hole activation
    based on the current score level.
    """
    # Initialize the main game graphics and object setup
    graphics = BreakoutGraphics()

    # Display the trash collection counter and lives label
    graphics.window.add(graphics.trash_collect, x=graphics.window.width-graphics.trash_collect.width-20,
                        y=graphics.window.height)
    graphics.window.add(graphics.live_label1, x=0, y=graphics.window.height)

    # Render and animate the opening story scene
    graphics.window.add(graphics.start_scene_bg)
    graphics.window.add(graphics.start_warning, x=(graphics.window.width - graphics.start_warning.width)/2,
                        y=(graphics.window.height-graphics.earth.height)//1.5-60)
    graphics.window.add(graphics.story_line0, x=(graphics.window.width - graphics.story_line0.width) / 2,
                        y=(graphics.window.height-graphics.earth.height)//1.5-20)
    graphics.window.add(graphics.earth, x=(graphics.window.width-graphics.earth.width)/2,
                        y=(graphics.window.height-graphics.earth.height)//1.25)
    graphics.window.add(graphics.story_line1, x=(graphics.window.width-graphics.story_line1.width)/2,
                        y=(graphics.window.height-graphics.earth.height)//1.5)
    graphics.window.add(graphics.story_line2, x=(graphics.window.width-graphics.story_line2.width)/2,
                        y=(graphics.window.height - graphics.earth.height) // 1.5+20)
    graphics.window.add(graphics.story_line3, x=(graphics.window.width-graphics.story_line3.width)/2,
                        y=(graphics.window.height - graphics.earth.height) // 1.5+40)
    graphics.window.add(graphics.story_line4, x=(graphics.window.width - graphics.story_line4.width)/2,
                        y=(graphics.window.height - graphics.earth.height) // 1.5 + 60)
    graphics.window.add(graphics.story_line5, x=(graphics.window.width - graphics.story_line5.width) / 2,
                        y=(graphics.window.height - graphics.earth.height) // 1.5 + 80)
    graphics.window.add(graphics.story_line6, x=(graphics.window.width - graphics.story_line6.width) / 2,
                        y=(graphics.window.height - graphics.earth.height) // 1.5 + 100)
    graphics.window.add(graphics.story_line7, x=(graphics.window.width - graphics.story_line7.width) / 2,
                        y=(graphics.window.height - graphics.earth.height) // 1.5 + 120)

    # Animate storyline text upward to transition into the game
    scene_ani_speed = -1
    global trash_switch
    while not graphics.story_line7.y <= 0:
        graphics.start_warning.move(0, scene_ani_speed)
        graphics.story_line0.move(0, scene_ani_speed)
        graphics.story_line1.move(0, scene_ani_speed)
        graphics.story_line2.move(0, scene_ani_speed)
        graphics.story_line3.move(0, scene_ani_speed)
        graphics.story_line4.move(0, scene_ani_speed)
        graphics.story_line5.move(0, scene_ani_speed)
        graphics.story_line6.move(0, scene_ani_speed)
        graphics.story_line7.move(0, scene_ani_speed)
        pause(5)
    graphics.window.remove(graphics.story_line0)
    graphics.window.remove(graphics.story_line1)
    graphics.window.remove(graphics.story_line2)
    graphics.window.remove(graphics.story_line3)
    graphics.window.remove(graphics.story_line4)
    graphics.window.remove(graphics.story_line5)
    graphics.window.remove(graphics.story_line6)
    graphics.window.remove(graphics.story_line7)
    graphics.window.remove(graphics.earth)
    graphics.window.add(graphics.click_to_start, x=(graphics.window.width-graphics.click_to_start.width)/2,
                        y=(graphics.window.height-graphics.click_to_start.height)/2)

    # Game state initialization: track attempts and brick status
    number_of_attempts = 0
    num_of_bricks = graphics.get_brick_num()
    number_of_brick_remove = 0
    black_hole_add_switch = True

    # Start the game loop: handles each ball drop sequence
    while True:
        if graphics.switch:
            graphics.window.remove(graphics.start_scene_bg)
            graphics.window.remove(graphics.click_to_start)
            vx = graphics.get_vx()
            vy = graphics.get_vy()

            # Speed boost at level 30 and 50
            if 30 <= graphics.trash < 50:
                vy = 12
            if 50 <= graphics.trash:
                vy = 15
            ball_speed_switch = True
            ball_speed_switch2 = True

            # moving speed of the rock above level 30
            black_hole_vx = 1
            black_hole_vy = 1
            rock_vx = 1
            rock_vy = 1
            rock_vx1 = 1
            rock_vy1 = 1
            rock_vx2 = 1
            rock_vy2 = 1
            rock_vx3 = 1
            rock_vy3 = 1
            rock_vx4 = 1
            rock_vy4 = 1

            # animation of ball
            while True:
                # Speed boost at level 30 and 50
                if graphics.trash == 30 and ball_speed_switch:
                    vy = 12
                    ball_speed_switch = False
                if graphics.trash == 50 and ball_speed_switch2:
                    vy = 15
                    ball_speed_switch2 = False
                # Move the ball according to current velocity
                graphics.ball.move(vx, vy)

                # Check ball collision with bricks or paddle
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
                    if may_be_obj.y == graphics.paddle.y:
                        graphics.window.add(graphics.ball, x=graphics.ball.x, y=graphics.paddle.y-graphics.ball.height)
                        vy = -vy
                    elif may_be_obj.y == graphics.window.height:
                        pass
                    elif may_be_obj == graphics.trash1:
                        pass
                    elif may_be_obj == graphics.trash2:
                        pass
                    elif may_be_obj == graphics.trash3:
                        pass
                    elif may_be_obj == graphics.trash4:
                        pass
                    elif may_be_obj == graphics.trash5:
                        pass
                    elif may_be_obj == graphics.trash6:
                        pass
                    elif may_be_obj == graphics.trash7:
                        pass
                    elif may_be_obj == graphics.trash8:
                        pass
                    elif may_be_obj == graphics.trash9:
                        pass
                    elif may_be_obj == graphics.warning_asteroid_belt:
                        pass
                    elif may_be_obj == graphics.black_hole_1:
                        pass
                    elif may_be_obj == graphics.black_hole_2:
                        pass
                    elif may_be_obj == graphics.black_hole_3:
                        pass
                    elif may_be_obj == graphics.black_hole_warning:
                        pass
                    elif may_be_obj == graphics.black_hole_warning1:
                        pass
                    elif may_be_obj == graphics.live_label1:
                        pass
                    else:
                        graphics.window.remove(may_be_obj)
                        number_of_brick_remove += 1
                        graphics.trash += 2
                        graphics.trash_collect.text = 'Trash You Collect ' + str(graphics.trash)
                        vy = -vy

                # Bounce the ball off the window borders
                if graphics.ball.x <= 0 or graphics.ball.x+graphics.ball.width >= graphics.window.width:
                    vx = -vx
                if graphics.ball.y <= 0:
                    vy = -vy

                # Handle when ball falls below the paddle
                if graphics.ball.y+graphics.ball.height >= graphics.window.height:
                    graphics.switch = False
                    graphics.window.add(graphics.ball, x=(graphics.window.width - graphics.ball.width)/2,
                                        y=(graphics.window.height - graphics.ball.height) / 2)
                    number_of_attempts += 1
                    if number_of_attempts == 1:
                        graphics.live_label1.text = '❤️❤️'
                    elif number_of_attempts == 2:
                        graphics.live_label1.text = '❤️'
                    elif number_of_attempts == 3:
                        graphics.live_label1.text = ''
                    break

                # Check win condition: all bricks cleared
                if number_of_brick_remove == num_of_bricks:
                    graphics.window.add(graphics.ball, x=(graphics.window.width - graphics.ball.width) / 2,
                                        y=(graphics.window.height - graphics.ball.height) / 2)
                    break

                # Trigger asteroid belt trash drop event every 10 points before level 30
                if graphics.trash != 0 and graphics.trash % 10 == 0 and graphics.trash < 30:
                    if trash_switch:
                        trash_switch = False
                        for i in range(4):
                            graphics.window.add(graphics.event_scene)
                            pause(50)
                            graphics.window.add(graphics.event_scene2)
                            pause(50)
                            graphics.window.remove(graphics.event_scene2)
                            pause(50)
                            graphics.window.remove(graphics.event_scene)
                            pause(50)
                        graphics.window.add(graphics.warning_asteroid_belt,
                                            x=(graphics.window.width-graphics.warning_asteroid_belt.width)//2,
                                            y=(graphics.window.height-graphics.warning_asteroid_belt.height)//2+100)
                        trash_x = random.randint(15, graphics.window.width-65)
                        graphics.window.add(graphics.trash1, x=trash_x, y=100)
                        trash_x = random.randint(15, graphics.window.width - 50)
                        graphics.window.add(graphics.trash2, x=trash_x, y=60)
                        trash_x = random.randint(15, graphics.window.width - 50)
                        graphics.window.add(graphics.trash3, x=trash_x, y=150)
                        trash_x = random.randint(15, graphics.window.width - 50)
                        graphics.window.add(graphics.trash4, x=trash_x, y=300)
                        trash_x = random.randint(15, graphics.window.width - 50)
                        graphics.window.add(graphics.trash5, x=trash_x, y=250)
                        trash_x = random.randint(15, graphics.window.width - 50)
                        graphics.window.add(graphics.trash6, x=trash_x, y=250)
                        trash_x = random.randint(15, graphics.window.width - 50)
                        graphics.window.add(graphics.trash7, x=trash_x, y=200)
                        trash_x = random.randint(15, graphics.window.width - 50)
                        graphics.window.add(graphics.trash8, x=trash_x, y=210)
                        trash_x = random.randint(15, graphics.window.width - 50)
                        graphics.window.add(graphics.trash9, x=trash_x, y=150)
                # Move falling trash until it leaves the window
                if not graphics.trash2.y >= graphics.window.height:
                    trash_vx = random.randint(-10, 10)
                    trash_vy = 1
                    graphics.trash1.move(trash_vx, trash_vy)
                    graphics.trash2.move(trash_vx, trash_vy)
                    graphics.trash3.move(trash_vx, trash_vy)
                    graphics.trash4.move(trash_vx, trash_vy)
                    graphics.trash5.move(trash_vx, trash_vy)
                    graphics.trash6.move(trash_vx, trash_vy)
                    graphics.trash7.move(trash_vx, trash_vy)
                    graphics.trash8.move(trash_vx, trash_vy)
                    graphics.trash9.move(trash_vx, trash_vy)

                # Clear trash and reset for next event
                else:
                    trash_switch = True
                    graphics.window.remove(graphics.trash1)
                    graphics.window.remove(graphics.trash2)
                    graphics.window.remove(graphics.trash3)
                    graphics.window.remove(graphics.trash4)
                    graphics.window.remove(graphics.trash5)
                    graphics.window.remove(graphics.trash6)
                    graphics.window.remove(graphics.trash7)
                    graphics.window.remove(graphics.trash8)
                    graphics.window.remove(graphics.trash9)
                    graphics.window.remove(graphics.warning_asteroid_belt)

                # Check if trash2 collides with paddle
                paddle_checker = False
                while True:
                    may_be_paddle = graphics.window.get_object_at(graphics.trash2.x, graphics.trash2.y)
                    if may_be_paddle is not None and may_be_paddle is graphics.paddle:
                        paddle_checker = True
                        break
                    may_be_paddle = graphics.window.get_object_at(graphics.trash2.x + graphics.trash2.width,
                                                                  graphics.trash2.y)
                    if may_be_paddle is not None and may_be_paddle is graphics.paddle:
                        paddle_checker = True
                        break
                    may_be_paddle = graphics.window.get_object_at(graphics.trash2.x,
                                                                  graphics.trash2.y + graphics.trash2.height)
                    if may_be_paddle is not None and may_be_paddle is graphics.paddle:
                        paddle_checker = True
                        break
                    may_be_paddle = graphics.window.get_object_at(graphics.trash2.x + graphics.trash2.width,
                                                                  graphics.trash2.y + graphics.trash2.height)
                    if may_be_paddle is not None and may_be_paddle is graphics.paddle:
                        paddle_checker = True
                        break
                    if not paddle_checker:
                        break
                if paddle_checker:
                    graphics.switch = False
                    graphics.window.add(graphics.ball, x=(graphics.window.width - graphics.ball.width) / 2,
                                        y=(graphics.window.height - graphics.ball.height) / 2)
                    number_of_attempts += 1
                    if number_of_attempts == 1:
                        graphics.live_label1.text = '❤️❤️'
                    elif number_of_attempts == 2:
                        graphics.live_label1.text = '❤️'
                    elif number_of_attempts == 3:
                        graphics.live_label1.text = ''
                    break

                # Check if trash4 collides with paddle
                paddle_checker = False
                while True:
                    may_be_paddle = graphics.window.get_object_at(graphics.trash4.x, graphics.trash4.y)
                    if may_be_paddle is not None and may_be_paddle is graphics.paddle:
                        paddle_checker = True
                        break
                    may_be_paddle = graphics.window.get_object_at(graphics.trash4.x + graphics.trash4.width,
                                                                  graphics.trash4.y)
                    if may_be_paddle is not None and may_be_paddle is graphics.paddle:
                        paddle_checker = True
                        break
                    may_be_paddle = graphics.window.get_object_at(graphics.trash4.x,
                                                                  graphics.trash4.y + graphics.trash4.height)
                    if may_be_paddle is not None and may_be_paddle is graphics.paddle:
                        paddle_checker = True
                        break
                    may_be_paddle = graphics.window.get_object_at(graphics.trash4.x + graphics.trash4.width,
                                                                  graphics.trash4.y + graphics.trash4.height)
                    if may_be_paddle is not None and may_be_paddle is graphics.paddle:
                        paddle_checker = True
                        break
                    if not paddle_checker:
                        break
                if paddle_checker:
                    graphics.switch = False
                    graphics.window.add(graphics.ball, x=(graphics.window.width - graphics.ball.width) / 2,
                                        y=(graphics.window.height - graphics.ball.height) / 2)
                    number_of_attempts += 1
                    if number_of_attempts == 1:
                        graphics.live_label1.text = '❤️❤️'
                    elif number_of_attempts == 2:
                        graphics.live_label1.text = '❤️'
                    elif number_of_attempts == 3:
                        graphics.live_label1.text = ''
                    break

                # Check if trash7 collides with paddle
                paddle_checker = False
                while True:
                    may_be_paddle = graphics.window.get_object_at(graphics.trash7.x, graphics.trash7.y)
                    if may_be_paddle is not None and may_be_paddle is graphics.paddle:
                        paddle_checker = True
                        break
                    may_be_paddle = graphics.window.get_object_at(graphics.trash7.x + graphics.trash7.width,
                                                                  graphics.trash7.y)
                    if may_be_paddle is not None and may_be_paddle is graphics.paddle:
                        paddle_checker = True
                        break
                    may_be_paddle = graphics.window.get_object_at(graphics.trash7.x,
                                                                  graphics.trash7.y + graphics.trash7.height)
                    if may_be_paddle is not None and may_be_paddle is graphics.paddle:
                        paddle_checker = True
                        break
                    may_be_paddle = graphics.window.get_object_at(graphics.trash7.x + graphics.trash7.width,
                                                                  graphics.trash7.y + graphics.trash7.height)
                    if may_be_paddle is not None and may_be_paddle is graphics.paddle:
                        paddle_checker = True
                        break
                    if not paddle_checker:
                        break
                if paddle_checker:
                    graphics.switch = False
                    graphics.window.add(graphics.ball, x=(graphics.window.width - graphics.ball.width) / 2,
                                        y=(graphics.window.height - graphics.ball.height) / 2)
                    number_of_attempts += 1
                    if number_of_attempts == 1:
                        graphics.live_label1.text = '❤️❤️'
                    elif number_of_attempts == 2:
                        graphics.live_label1.text = '❤️'
                    elif number_of_attempts == 3:
                        graphics.live_label1.text = ''
                    break

                # Check if trash9 collides with paddle
                paddle_checker = False
                while True:
                    may_be_paddle = graphics.window.get_object_at(graphics.trash9.x, graphics.trash9.y)
                    if may_be_paddle is not None and may_be_paddle is graphics.paddle:
                        paddle_checker = True
                        break
                    may_be_paddle = graphics.window.get_object_at(graphics.trash9.x + graphics.trash9.width,
                                                                  graphics.trash9.y)
                    if may_be_paddle is not None and may_be_paddle is graphics.paddle:
                        paddle_checker = True
                        break
                    may_be_paddle = graphics.window.get_object_at(graphics.trash9.x,
                                                                  graphics.trash9.y + graphics.trash9.height)
                    if may_be_paddle is not None and may_be_paddle is graphics.paddle:
                        paddle_checker = True
                        break
                    may_be_paddle = graphics.window.get_object_at(graphics.trash9.x + graphics.trash9.width,
                                                                  graphics.trash9.y + graphics.trash9.height)
                    if may_be_paddle is not None and may_be_paddle is graphics.paddle:
                        paddle_checker = True
                        break
                    if not paddle_checker:
                        break
                if paddle_checker:
                    graphics.switch = False
                    graphics.window.add(graphics.ball, x=(graphics.window.width - graphics.ball.width) / 2,
                                        y=(graphics.window.height - graphics.ball.height) / 2)
                    number_of_attempts += 1
                    if number_of_attempts == 1:
                        graphics.live_label1.text = '❤️❤️'
                    elif number_of_attempts == 2:
                        graphics.live_label1.text = '❤️'
                    elif number_of_attempts == 3:
                        graphics.live_label1.text = ''
                    break

                # Trigger black hole and rock field appearance at level 30+
                if graphics.trash >= 30:
                    paddle_vx = random.randint(-10, 10)
                    graphics.paddle.move(paddle_vx, 0)
                    if black_hole_add_switch:
                        graphics.window.add(graphics.black_hole_warning,
                                            x=(graphics.window.width-graphics.black_hole_warning.width)//2,
                                            y=(graphics.window.height-graphics.warning_asteroid_belt.height)//2+100)
                        graphics.window.add(graphics.black_hole_warning1,
                                            x=(graphics.window.width - graphics.black_hole_warning1.width) // 2,
                                            y=(graphics.window.height - graphics.warning_asteroid_belt.height)//2+150)
                        graphics.window.add(graphics.black_hole_1, x=(graphics.window.width-graphics.black_hole_1.width)/2,
                                            y=(graphics.window.height-graphics.black_hole_1.height)/2)
                        graphics.window.add(graphics.black_hole_2,
                                            x=(graphics.window.width - graphics.black_hole_1.width)/2+10,
                                            y=(graphics.window.height - graphics.black_hole_1.height)/2+10)
                        graphics.window.add(graphics.black_hole_3,
                                            x=(graphics.window.width - graphics.black_hole_1.width)/2+20,
                                            y=(graphics.window.height - graphics.black_hole_1.height)/2+20)
                        graphics.window.add(graphics.rock, x=80, y=200)
                        graphics.window.add(graphics.rock1, x=280, y=400)
                        graphics.window.add(graphics.rock2, x=400, y=180)
                        graphics.window.add(graphics.rock3, x=600, y=110)
                        graphics.window.add(graphics.rock4, x=550, y=270)
                        black_hole_add_switch = False
                    else:
                        graphics.black_hole_1.move(black_hole_vx, black_hole_vy)
                        graphics.black_hole_2.move(black_hole_vx, black_hole_vy)
                        graphics.black_hole_3.move(black_hole_vx, black_hole_vy)
                        graphics.rock.move(rock_vx, rock_vy)
                        graphics.rock1.move(rock_vx1, rock_vy1)
                        graphics.rock2.move(rock_vx2, rock_vy2)
                        graphics.rock3.move(rock_vx3, rock_vy3)
                        graphics.rock4.move(rock_vx4, rock_vy4)
                        if graphics.black_hole_1.x <= 0 or graphics.black_hole_1.x >= graphics.window.width:
                            black_hole_vx = -black_hole_vx
                        if graphics.black_hole_1.y <= 0 or graphics.black_hole_1.y >= graphics.window.height/2:
                            black_hole_vy = -black_hole_vy
                        if graphics.rock.x <= 0 or graphics.rock.x >= graphics.window.width:
                            rock_vx = -rock_vx
                        if graphics.rock1.x <= 0 or graphics.rock1.x >= graphics.window.width:
                            rock_vx1 = -rock_vx1
                        if graphics.rock2.x <= 0 or graphics.rock2.x >= graphics.window.width:
                            rock_vx2 = -rock_vx2
                        if graphics.rock3.x <= 0 or graphics.rock3.x >= graphics.window.width:
                            rock_vx3 = -rock_vx3
                        if graphics.rock4.x <= 0 or graphics.rock4.x >= graphics.window.width:
                            rock_vx4 = -rock_vx4
                        if graphics.rock.y <= 0 or graphics.rock.y+graphics.rock.height >= graphics.window.height:
                            rock_vy = -rock_vy
                        if graphics.rock1.y <= 0 or graphics.rock1.y+graphics.rock1.height >= graphics.window.height:
                            rock_vy1 = -rock_vy1
                        if graphics.rock2.y <= 0 or graphics.rock2.y+graphics.rock2.height >= graphics.window.height:
                            rock_vy2 = -rock_vy2
                        if graphics.rock3.y <= 0 or graphics.rock3.y+graphics.rock3.height >= graphics.window.height:
                            rock_vy3 = -rock_vy3
                        if graphics.rock4.y <= 0 or graphics.rock4.y+graphics.rock4.height >= graphics.window.height:
                            rock_vy4 = -rock_vy4
                # pause
                pause(FRAME_RATE)
        else:
            graphics.ball.move(0, 0)
        pause(FRAME_RATE)
        # Check if game over by losing all lives or winning by clearing all bricks
        if number_of_attempts == NUM_LIVES:
            graphics.window.add(graphics.lose_bg, x=0, y=0)
            graphics.window.add(graphics.lose_img, x=(graphics.window.width - graphics.lose_img.width) // 2,
                                y=graphics.window.height - graphics.lose_img.height)
            break
        if number_of_brick_remove == num_of_bricks:
            graphics.window.add(graphics.win_bg, x=0, y=0)
            graphics.window.add(graphics.win_img, x=(graphics.window.width-graphics.win_img.width)//2,
                                y=graphics.window.height-graphics.win_img.height)
            break















if __name__ == '__main__':
    main()
