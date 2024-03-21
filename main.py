import pygame as pg
from pygame import draw
import numpy as np
from player import Player
from math import exp
import sys
sWidth = 640
sHeigth = 480
# mapa
cols = 20
rows = 15
tiles = []
tiles.append(pg.image.load("./sprites/Ground.png"))
tiles.append(pg.image.load("./sprites/Grass.png"))



map_info=  [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
            [2,1,1,1,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
            [2,1,1,1,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
            [2,1,1,1,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
            [2,1,1,1,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
            [2,1,1,1,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
            [2,1,1,1,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
            [2,1,1,1,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
            [3,3,3,3,3,3,3,0,0,0,3,3,3,3,3,3,3,3,3,3],
            [2,2,2,2,2,2,2,0,0,0,2,2,2,2,2,2,2,2,2,2],
            [2,2,2,2,2,2,2,0,0,0,2,2,2,2,2,2,2,2,2,2],
            [2,2,2,2,2,2,2,0,0,0,2,2,2,2,2,2,2,2,2,2]]

print(map_info)

# jugador
player = Player("./sprites/PlaceHoldPNJ.png",[0,0])


pg.init()

## escenario ##
screen = pg.display.set_mode((sWidth,sHeigth))
def DrawScene():
    screen.fill((32,127,238))
    for col_index,col in enumerate(map_info):
        for item_item,item in enumerate(col):
            if item == 2:
                screen.blit(tiles[0],(32*item_item,32*col_index))
            elif item == 3:
                screen.blit(tiles[1],(32*item_item,32*col_index))
            

while(1):
    DrawScene()
    screen.blit(player.model,player.pos)
    #control de colisiones del personaje
    print(map_info[int((player.rect[3])/32)][int((player.rect[0]+16)/32)])
    if(map_info[int((player.rect[3])/32)][int((player.rect[0]+16)/32)] <2):
        player.onGround = False
    else:
        player.onGround = True
    
    if(map_info[int((player.rect[1]+16)/32)][int(player.rect[0]/32)] > 1):
        player.onGroundHL = True
    else:
        player.onGroundHL = False
    if(map_info[int((player.rect[1]+16)/32)][int(player.rect[2]/32)] > 1):
        player.onGroundHR = True
    else:
        player.onGroundHR = False
    
    if(not player.onGround):
        if(player.jumping == 0):
            player.move(0,1*player.gravity)
    player.update()
    
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
            
    pg.display.flip()    
    pg.time.Clock().tick(60)