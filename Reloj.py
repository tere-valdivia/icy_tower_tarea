#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  6 10:04:49 2017

@author: terevaldivia
"""

import os
from CC3501Utils_personal import *

pi = 3.1415
fps = 60
clock = pygame.time.Clock()

class Reloj(Figura):
    #variables de instancia del palito
    tamano = 24.
    segundo = 0.
    x_palito = 0
    y_palito = tamano #posiciones iniciales
    seg_final = 30
    
    def __init__(self, pos=Vector(0, 0), rgb=(1.0, 1.0, 1.0)):
        super(Reloj, self).__init__(pos, rgb)
    def figura(self):
        
        #Base circular
        glBegin(GL_TRIANGLE_FAN)
        glColor3f(47 / 255.0, 79 / 255.0, 79 / 255.0)
        glVertex2f(0.0, 0.0)

        radio1 = 30
        ang = 2 * pi / 20
        for i in range(20):
            ang_i = ang * i
            glVertex2f(cos(ang_i) * radio1, sin(ang_i) * radio1)

        glVertex2f(1.0 * radio1, 0.0)
        glEnd()
        
        #Circulo interior
        glBegin(GL_TRIANGLE_FAN)
        glColor3f(97 / 255.0, 218 / 255.0, 137 / 255.0) 
        glVertex2f(0.0, 0.0)

        radio2 = 24
        ang = 2 * pi / 20
        for i in range(20):
            ang_i = ang * i
            glVertex2f(cos(ang_i) * radio2, sin(ang_i) * radio2)

        glVertex2f(1.0 * radio2, 0.0)
        glEnd()
        
        #palillo: que sea actualizable con variables de instancia afuera
        glBegin(GL_LINES)
        glColor3f(0 / 255.0, 0 / 255.0, 0 / 255.0) #negro?
        glVertex2f(0.0, 0.0)
        glVertex2f(self.x_palito, self.y_palito)
        glEnd()

    def update(self, fps):
        self.segundo += 1./fps
        if self.segundo >= self.seg_final:
            return
        self.x_palito = self.tamano * sin(pi * self.segundo / 30.)
        self.y_palito = self.tamano * cos(pi * self.segundo / 30.)