import pgzrun as pg
import os
import time
from random import *

egg = Actor('rene')
bird = Actor('bird')
WIDTH = 500
HEIGHT = 500
bird.center
score = 0
game_over = False


bird_y = 200
bird_y_speed = 0

def update(dt):
    global bird_y, bird_y_speed
    bird_y += 30 * dt
    bird_y_speed += 516 * dt
    bird_y += bird_y_speed * dt
    bird_y = int(bird_y)

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
    
def on_key_down():
    global bird_y_speed
    if bird_y > 0:
        bird_y_speed = -165


pg.go()
