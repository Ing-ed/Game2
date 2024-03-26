import pygame as pg
import time
class Player:
    def __init__(self,model,initPos):
        self.models = model
        self.model = pg.image.load(model[0])
        self.width = self.model.get_rect()[2]
        self.heigh = self.model.get_rect()[3]
        self.rotation = 0
        self.pos = initPos
        self.rect = pg.Rect(self.pos[0],self.pos[1],self.width + self.pos[0],self.heigh + self.pos[1])
        self.onGround = False
        self.onGroundHL = False
        self.onGroundHR = False
        self.jumping = 0
        self.speed = 4
        self.gravity = 5
        self.velocity = [0,0]
        self.jumpDistance = 5
        self.animate = 0    
        self.animateFrames = 5
        self.animateFramesDef = 5

    def move(self,despX = 0,despY = 0):
        self.width = self.model.get_rect()[2]
        self.heigh = self.model.get_rect()[3]
        self.pos[0] += despX
        self.pos[1] += despY
        self.rect = pg.Rect(self.pos[0],self.pos[1],self.width + self.pos[0],self.heigh + self.pos[1])
        # self.model = pg.transform.rotate(self.model,1) if self.rotation 
    
    def jump(self):
        self.move(self.velocity[0],-15)
        self.jumping -= 1

    def update(self,canHor = True, canVert = True):
        
        if(self.jumping):
            if(self.jumping > 0):
                self.jump()
            
        keys = pg.key.get_pressed()
        if(keys[pg.K_a]):
            if(not self.onGroundHL):
                self.move(-1*self.speed,0)#self.pos[0]-= 1
                self.velocity = [-1*self.speed,0]
                if(self.animateFrames == 0):
                    self.model = pg.transform.flip(pg.image.load(self.models[self.animate]),True,False) if self.animateFrames == 0 else None
                self.animateFrames = self.animateFrames - 1 if self.animateFrames > 0 else 10
                self.animate = self.animate+1 if self.animate < len(self.models)-1 else 0
                # pg.transform.flip(self.model,True,True)
        if(keys[pg.K_d]):
            if(not self.onGroundHR):
                self.move(1*self.speed,0)#self.pos[0]+= 1
                self.velocity = [1*self.speed,0]
                if(self.animateFrames == 0):
                    self.model = pg.image.load(self.models[self.animate])if self.animateFrames == 0 else None
                self.animateFrames = self.animateFrames - 1 if self.animateFrames > 0 else 10
                self.animate = self.animate+1 if self.animate < len(self.models)-1 else 0
        if(keys[pg.K_s]):
            if(not self.onGround):
                self.move(0,1)#self.pos[1] += 1
        if(keys[pg.K_w]):
            if(not self.onGround):
                self.move(0,-1)#self.pos[0]+= 1
        if(keys[pg.K_SPACE]):
            if(self.onGround):
                print("Salto")
                if(self.jumping == 0):
                    self.jumping = self.jumpDistance
        else:
            self.velocity = [0,0]