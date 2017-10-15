#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 11:46:51 2017

@author: terevaldivia
"""
import os
from CC3501Utils_personal import *
import numpy as np

class Fondo(Figura):
    
    def __init__(self, pos=Vector(0, 0), rgb=(1.0, 1.0, 1.0)):
        super(Fondo, self).__init__(pos, rgb)
        
    def figura(self):
        glBegin(GL_QUADS)
        glColor3f(80 / 255.0, 80 / 255.0, 80 / 255.0)  #gris oscuro
        glVertex2f(0,0)
        glVertex2f(0, 600)
        glVertex2f(800, 600)
        glVertex2f(800, 0)
        glEnd()
        
        numx = np.linspace(0., 700., 5)
        numy = np.linspace(0., 500., 5)
        altura = 30.
        ancho = 50.
        
        for x in numx:
            for y in numy:
                glBegin(GL_QUADS)
                glColor3f(66 / 255.0, 74 / 255.0, 65 / 255.0)  #gris oscuro
                glVertex2f(x, y)
                glVertex2f(x, y + altura)
                glVertex2f(x + ancho, y + altura)
                glVertex2f(x + ancho, y)
                glEnd()
                glBegin(GL_QUADS)
                glColor3f(50 / 255.0, 50 / 255.0, 50 / 255.0)  #gris oscuro
                glVertex2f(x+20, y+30)
                glVertex2f(x+20, y +30  + altura)
                glVertex2f(x+20 + ancho, y+30 + altura)
                glVertex2f(x+20 + ancho, y+30)
                glEnd()
        