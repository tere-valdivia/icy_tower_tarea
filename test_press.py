#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 17:28:55 2017

@author: terevaldivia
"""
import pygame
pygame.init()

display = pygame.display.set_mode((100,100))

clock = pygame.time.Clock()

while True:
    pygame.event.pump()
    keypressed = pygame.key.get_pressed()

    if keypressed[pygame.K_w]:
        print("it worked")
    else: 
        print("It didn't work")

    #compute how many milliseconds have passed since the previous call
    clock.tick(30)