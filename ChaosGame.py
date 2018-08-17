import pygame
import random
from random import randint
from time import *


def midpoint(x1,y1,x2,y2): #function to comoute the midpoint
    x=(x1+x2)/2
    y=(y1+y2)/2
    return x,y


black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)

pygame.init()
size = [1024, 1024]
screen=pygame.display.set_mode(size)
pygame.display.set_caption("Chaos Game")
done = False
clock = pygame.time.Clock()


while done is False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    screen.fill(white)
    screen.set_at((100, 200), black)
    x=300
    y=300
    for i in range(0,10000):#the process is repeated 10000 times
        pygame.time.wait(1)
        a=random.randint(1,3) # genrating a random number in between 1 and 3
        if a==1:
            x,y=midpoint(x,y,500,100)
        elif a==2:
            x,y=midpoint(x,y,200,500)
        elif a==3:
            x,y=midpoint(x,y,800,500)
        pygame.draw.line(screen,black,[x,y],[x,y+2],5)
    clock.tick(20)
    pygame.display.flip()

pygame.quit ()
