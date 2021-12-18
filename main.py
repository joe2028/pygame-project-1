import pgzrun as pg
import os
import time
from random import *

#egg = Actor('rene')
bird = Actor('bird')
WIDTH = 500
HEIGHT = 500
bird.center
score = 0
game_over = False

pipe_1_x = 100
pipe_1_space_y = 100

pipe_2_x = 200
pipe_2_space_y = 200

bird_y = 200
bird_y_speed = 0



def update(dt):
    global bird_y, bird_y_speed
    bird_y += 30 * dt
    bird_y_speed += 516 * dt
    bird_y += bird_y_speed * dt
    bird_y = int(bird_y)
    if bird_y <= 0:
        game_over = True


def draw():
    screen.clear()
    
    screen.fill((255,255,255))
    screen.draw.filled_rect(
        Rect(
            (0,0),
            (500, 500)
            ),
            color=(35, 92, 118)
        )
    bird.draw()
    bird.y = bird_y
    if bird_y >= 500:
        screen.draw.text("GAME OVER", center=(250, 250), fontsize=32)
    
def draw_pipe(pipe_x, pipe_space_y):
    screen.draw.filled_rect(
        Rect(
            (pipe_x, 0),
            (pipe_width, pipe_space_y)
            ),
            color=(94, 201, 72)
        )

    screen.draw.filled_rect(
        Rect(
            (pipe_x, pipe_space_y + pipe_space_height),
                (pipe_width, playing_area_height - pipe_space_y - pipe_space_height)
            ),
            color=(94, 201, 72)
        )

draw_pipe(pipe_1_x, pipe_1_space_y)
draw_pipe(pipe_2_x, pipe_2_space_y)


def on_key_down():
    if bird_y >= 500:
        pass
    else:
        global bird_y_speed
        if bird_y > 0:
            bird_y_speed = -165

pg.go()
