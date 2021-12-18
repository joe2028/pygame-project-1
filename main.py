import pgzrun as pyg
from random import *
import time

alien = Actor('alien')
WIDTH = 1000
HEIGHT = alien.height + 500
alien.center
score = 0
game_over = False

egg = Actor('rene')
egg.center = (randint(25, 500), randint(50, 500))

startTime = time.time()
time_elasped = 0

def check_egg_collection():
    global alien, egg, score
    if(egg.colliderect(alien)):
        score += 1
        egg.center = (randint(0, 1000), randint(0, 685))


    #if game_over == True:
       # screen.draw.text('GAME OVER!!!', topright = (100, 50), fontsize = 64, color="black")
       # sounds.damndaniel.play()
    else:
        if keyboard.left:
            alien.x -= 5
            if alien.x <= 0:
                alien.right = 1000
        elif keyboard.right:
            alien.x += 5
            if alien.right > WIDTH:
                alien.left = 0
        elif keyboard.up:
            alien.y -= 5
            if alien.y <= 0:
                alien.y = 300
        elif keyboard.down:
            alien.y += 5
            if alien.y >= 683 and alien.x >= 5:
                alien.y = 0
                sounds.scary.play()

if game_over == True:
        screen.draw.text('GAME OVER!!!', topright = (100, 50), fontsize = 64, color="black")
        sounds.damndaniel.play()



def draw():
    global score, egg
    screen.clear()
    screen.fill((255, 255, 255))
    if game_over == True:
        screen.draw.text('GAME OVER!!!', topright = (100, 50), fontsize = 64, color="black")
    screen.draw.text('Time left: ' + str(60 - time_elasped), topright = (380, 20), fontsize = 32, color="black")
    screen.draw.text('Score: ' + str(score), topleft = (100, 50), fontsize = 32, color="black")
    egg.draw()
    alien.draw()

def set_alien_normal():
    alien.image = 'alien'

def set_alien_hurt():
    aline.image = 'alien_hurt'

def update():
    global time_elasped
    time_elasped = int(time.time() - startTime)
    check_egg_collection()
    if score >= 100:
        screen.draw.text('YOU WIN!', center = (500, 300), fontsize = 65, color="black")
    if time_elasped >= 60:
        game_over = True
        screen.draw.text('GAME OVER!!!', topright = (100, 50), fontsize = 64, color="black")
        sounds.damndaniel.play()

pyg.go()
