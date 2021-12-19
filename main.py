import pgzrun as pg
import os
import time
from random import *



TITLE = 'Mutated Flappy Bird'

egg = Actor('rene', center=(200, 400))
gap = 140
bird = Actor('bird', (75, 350))
WIDTH = 400
HEIGHT = 708
score = 0
game_over = False

top_pipe = Actor('top', (300, 0))
bottom_pipe = Actor('bottom', (300, top_pipe.height + gap))

pipe_1_x = 100
pipe_1_space_y = 100

pipe_2_x = 200
pipe_2_space_y = 200

bird_y = 200


def update(dt):
    global bird_y, bird_y_speed, scroll_speed
    bird_y += 30 * dt
    bird_y_speed += 516 * dt
    bird_y += bird_y_speed * dt
    bird_y = int(bird_y)
    scroll_speed = -2
    top_pipe.x += scroll_speed
    bottom_pipe.x += scroll_speed
    offset = randint(-150, 200)

    if top_pipe.x < -20:
        #top_pipe.x = WIDTH
        top_pipe.midleft = (WIDTH, offset)
    if bottom_pipe.x < -20:
        #bottom_pipe.x = WIDTH
        bottom_pipe.midleft = (WIDTH, offset + top_pipe.height + 200)

    if (bird.colliderect(top_pipe)) or (bird.colliderect(bottom_pipe)):
        hit_pipe()
    if bird_y <= 0 :
        game_over = True
    if bird.alive:
        if top_pipe.right < bird.x :
            bird.score += 1



def draw() :
    global scroll_speed
    screen.clear()
    screen.fill((255, 255, 255))
    screen.blit('background', (0, 0))
    top_pipe.draw()
    bottom_pipe.draw()
    bird.draw()
    bird.y = bird_y
    if bird_y >= 500 :
        screen.draw.text("GAME OVER", center=(200, 300), fontsize=60, owidth=1.5, ocolor=(0, 0, 0), color='orange')
        scroll_speed = 1
        sounds.damndaniel.play()
        egg.draw()
    elif bird_y > HEIGHT :
        reset()
    screen.draw.text(
        str(bird.score),
        color='white',
        midtop=(20, 10),
        fontsize=70,
        owidth=1.5,
        ocolor='black'
    )


def on_key_down() :
    if (bird.alive):
        if bird_y >= 500:
            pass
        else :
            global bird_y_speed
            if bird_y > 0 :
                bird_y_speed = -165
    else:
        screen.draw.text("GAME OVER", center=(200, 300), fontsize=60, owidth=40, ocolor=(0, 0, 255), color='orange')


def reset() :
    global bird_y_speed
    bird_y_speed = 1
    bird.center = (75, 350)
    top_pipe.center = (300, 0)
    bottom_pipe.center = (300, top_pipe.height + gap)
    bird.alive = True
    top_pipe.pair_number = 1

def hit_pipe():
    screen.draw.text("GAME OVER", center=(200, 300), fontsize=60, owidth=40, ocolor=(0,0,255), color='orange')
    bird.alive = False

bird.score = 0

reset()
pg.go()
