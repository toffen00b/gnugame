from pygame import *
import random

size_fon= 1
a = ['Visit GNU.org' , 'Visit fsf.org' , 'Visit hyperbola.info' , 'Install Trisquel GNU/Linux-libre' , 'GNU is not UNIX' , 'Install Parabola GNU/Linux-libre' , 'Install Hyperbola GNU/Linux-libre']

init()
#screen = display.set_mode((480 * size_fon, 270 * size_fon ))
screen = display.set_mode((480, 270))
display.set_caption(random.choice(a))
from tkinter import *
from tkinter import messagebox
Tk().wm_withdraw() 
messagebox.showinfo('Start Game?')

#size_fon= 2
game_on = 1
x, y = 100,100
FPS = time.Clock()
fon = image.load('i.jpg')
#fon = transform.scale(fon, (350 * size_fon, 350 * size_fon))
block = image.load('ch2.png')
block = transform.scale(block,(200,200))
while game_on:
    screen.blit(fon, (0,0))
    #draw.circle(screen, (100, 100, 100),(x,y), 50 )
    #draw.image(screen, (x,y), 50 )
    screen.blit(block, (x, y))
    display.flip()
    b = key.get_pressed()
    if b[K_LEFT]:
        x -= 1
    elif b[K_RIGHT]:
        x += 1
    elif b [K_UP]:
        y -= 1
    elif b[K_DOWN]:
        y += 1
    for sobytie in event.get():
        if sobytie.type == QUIT:
            game_on = 0
    FPS.tick(780)
quit()