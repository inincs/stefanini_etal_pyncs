import pygame, sys
from pygame.locals import *

pygame.init()
fpsClock = pygame.time.Clock()

win_width, win_height = 640, 480
windowSurfaceObj = pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption('Sliding bar')

grayColor = pygame.Color(0, 0, 0)
bars_contrast = 0.1 # luminance contrast between bars
bar1Color = pygame.Color(255, 255, 255)
bar2Color = pygame.Color(255-int(bars_contrast*255),
                         255-int(bars_contrast*255),
                         255-int(bars_contrast*255))

pos_left1 = 10 # initial position of the bar1
pos_top1 = 10
delta_left1 = 5
delta_top1 = 5
width1 = 100
height1 = 20

pos_left2 = -10 # initial position of the bar
pos_top2 = 10
delta_left2 = -5
delta_top2 = -5
width2 = 50
height2 = 20

while True:
    windowSurfaceObj.fill(grayColor)

    pygame.draw.rect(windowSurfaceObj,
                     bar1Color,
                     (pos_left1, pos_top1, width1, height1))

    pygame.draw.rect(windowSurfaceObj,
                     bar2Color,
                     (pos_left2, pos_top2, width2, height2))

    pos_top1 += delta_top1
    pos_left1 += delta_left1
    pos_left1 %= win_width - width1
    pos_top1 %= win_height - height1

    pos_top2 += delta_top2
    pos_left2 += delta_left2
    pos_left2 %= win_width - width2
    pos_top2 %= win_height - height2

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    fpsClock.tick(20)
