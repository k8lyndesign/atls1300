#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""


@author: kaitlynengelson

Modified IC script! 

PSEUDOCODE
create robot - square head, line and circle for antenna, circles for eyes, 
rectangle mouth, trapezoid body with circles for buttons, lines and arcs for 
arms, and black circles for wheels
make him moveable with arrow keys 
make his eyes grow with keys 
make his eyes change colors with keys 

"""

import pygame
from random import *

#set up colors
BLACK = (0,0,0)
RED = (255,0,0)
PINK = (170,0,50)
GREEN = (0,255,0)
BLUE = (0,0,255)
LT_BLUE = (0, 100, 255)
WHITE = (255,255,255)
GRAY = (127,127,127)
DK_GRAY = (100,100,100)

#create screen and game variables
size = 500
screen = pygame.display.set_mode((size,size)) #create 500 x500 pixel screen

run = True
x = size/2 #center position for all robot parts
y = size/2
scale = 1 #variable to adjust when keys are pressed to change size of robot
vel = 2
eye_r = 2

#Robo features
blink = [GREEN, BLUE, RED, LT_BLUE]
color = choice(blink) #assign a value to color
colorL = choice(blink) #assign a value to color
colorR = choice(blink) #assign a value to color

#Game loop
while run:
    # create exit-on click detection:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            run = False
            
    #Drawing goes from bottom to top. We'll make our screen white first, then
    #add the robo-parts.    
    screen.fill(WHITE)
    
    #Pygame draw docs: https://www.pygame.org/docs/ref/draw.html#pygame.draw.circle
    
    keyz = pygame.key.get_pressed() #check for any keys that are pressed , make roboguy move
    if keyz[pygame.K_RIGHT]:
        x += vel
    if keyz[pygame.K_LEFT]:
        x -= vel
    if keyz[pygame.K_UP]:
        y -= vel
    if keyz[pygame.K_DOWN]:
        y += vel
        
    if keyz[pygame.K_SPACE]:#make eyez bigger!!
        if eye_r<=10:
            eye_r+=10
        elif eye_r > 10: 
            eye_r-= 10 
 
            
     #robo-partz   
    screen.fill(WHITE)  
    Head = pygame.draw.rect(screen,GRAY,(x-25,y-90,50,50)) 
    Body = pygame.draw.polygon(screen, GRAY, [(x+35, y-35),(x+45,y+35), (x-45,y+35),(x-35, y-35)])
    L_eye = pygame.draw.circle(screen, GREEN, (int(x-10), int(y-70)),eye_r)
    R_eye = pygame.draw.circle(screen, GREEN, (int(x+10), int(y-70)),eye_r)
    panelLights1 = pygame.draw.circle(screen, colorR, (int(x+20), int(y-5)),3)
    panelLights2 = pygame.draw.circle(screen, color, (int(x), int(y-5)),3)
    panelLights3 = pygame.draw.circle(screen, colorL, (int(x-20), int(y-5)),3)

    L_wheel = pygame.draw.circle(screen, BLACK, (int(x-40), int(y+63)),20)
    R_wheel = pygame.draw.circle(screen, BLACK, (int(x+40), int(y+63)),20)
    L_hub = pygame.draw.circle(screen, DK_GRAY, (int(x-40), int(y+63)),10)
    R_hub = pygame.draw.circle(screen, DK_GRAY, (int(x+40), int(y+63)),10)
    Track = pygame.draw.ellipse(screen, DK_GRAY, (int(x-65), int(y+33),130,60),2)

    pygame.display.update() #update all changes to screen