#!/usr/bin/python3
import pygame, math, numpy as np

ratio = int(input("What is the mass of the larger object?: "))
pygame.init()
win = pygame.display.set_mode([1920, 1080])
clock = pygame.time.Clock()
run = True

class obj1:
    def __init__(self):
        self.mass = 1
        self.invel = 0
        self.vel = 0
        self.x = 400 # Y-pos wil always be 900
    def draw(self):
        pygame.draw.rect(win, (255, 0, 0), (self.x, 900, 80, 80))

class obj2:
    def __init__(self):
        self.mass = ratio
        self.invel = 0
        self.vel = -4
        self.x = 800 # Y-pos wil always be 900
    def draw(self):
        vlu = 80*(int(math.log(self.mass, 100))+1)
        pygame.draw.rect(win, (255, 0, 0), (self.x, 980-vlu, vlu, vlu))

smo = obj1()
bgo = obj2()
while run:
    totalMomentum = smo.vel + (ratio*bgo.vel)
    totalKinetic = (0.5*(smo.vel**2)) + (0.5*ratio*(bgo.vel**2))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    win.fill((255, 255, 255))
    pygame.draw.rect(win, (0, 0, 0), (100, 0, 1820, 980))
    smo.draw()
    bgo.draw()
    if smo.x <= 103:
        smo.x = 100
        smo.invel = smo.vel
        smo.vel *= -1
    if bgo.x - smo.x <= 80:
        m1 = bgo.mass
        m2 = smo.mass
        bgo.invel = bgo.vel
        smo.invel = smo.vel
        velbgo = ((m1 - m2)/(m1 + m2))*bgo.invel
        #print(velbgo)
        bgo.vel = velbgo
        velsmo = ((2*m1)/(m1+m2))*bgo.invel
        smo.vel = velsmo
        #print(velsmo)
        """ a = (smo.mass * bgo.mass) + (smo.mass**2)
        b = -2*(smo.mass**2)*smo.vel + 2*smo.mass*bgo.mass*bgo.vel
        c = smo.mass**2 * smo.vel**2 + 2*smo.mass*bgo.mass*smo.vel**2
        d = b**2 - 4*a*c
        bgo.invel = bgo.vel
        if d < 0:
            print("Fail")
            break
        poss1 = ( - b + math.sqrt(d))/(2*a)
        poss2 = ( - b - math.sqrt(d))/(2*a)
        print(poss1)
        smo.invel = smo.vel
        smo.vel = poss1*-1
#        if poss1 < 0:
#            smo.invel = smo.vel
#            smo.vel = poss2*-1
#        else:
#            smo.invel = smo.vel
#            smo.vel = poss1*-1
        bgo.vel = (smo.mass*smo.invel + bgo.mass*bgo.invel - smo.mass*smo.vel)/bgo.mass
        print(smo.vel, bgo.vel)
        # now put these values in momentum equation
        # you will get two values for v2-prime
        # one of them will not make sense from physics point of view

        #vel*bgo.vel - smo.mass*bgo.mass*smo.vel**2 """
    smo.x += smo.vel
    bgo.x += bgo.vel
    print(smo.vel, bgo.vel)
    pygame.display.update()
    clock.tick(60)