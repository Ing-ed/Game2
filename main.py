import pygame as pg
from pygame import draw
import numpy as np
from math import exp
import sys
sWidth = 640
sHeigth = 480
cols = 20
rows = 15
tiles = []
tiles.append(pg.image.load("./sprites/Ground.png"))
tiles.append(pg.image.load("./sprites/Grass.png"))

map_info=  [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]
print(map_info)

pg.init()

## escenario ##
screen = pg.display.set_mode((sWidth,sHeigth))
def DrawScene():
    screen.fill((32,127,238))
    for i in range(0,cols):
        # for j in range(10,rows):
        screen.blit(tiles[1],(32*i,32*9))
    for i in range(0,cols):
        for j in range(10,rows):
            screen.blit(tiles[0],(32*i,32*j))


while(1):
    DrawScene()
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
            
    pg.display.flip()