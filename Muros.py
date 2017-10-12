#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  6 15:27:08 2017

@author: terevaldivia
"""

import os
from CC3501Utils_personal import *
import numpy as np

class Muros(Figura):
    
    def __init__(self, pos=Vector(0, 0), rgb=(1.0, 1.0, 1.0)):
        super(Muros, self).__init__(pos, rgb)
    
    def figura(self):
        
        #tomamos el origen como la esquina inferior izquierda
        
        #bases cuadradas
        glBegin(GL_QUADS)
        glColor3f(105 / 255.0, 105 / 255.0, 105 / 255.0)  #gris oscuro
        glVertex2f(0,0)
        glVertex2f(0, 600)
        glVertex2f(40, 600)
        glVertex2f(40, 0)
        glEnd()
        glBegin(GL_QUADS)
        glColor3f(105 / 255.0, 105 / 255.0, 105 / 255.0)  #gris oscuro
        glVertex2f(800,0)
        glVertex2f(800, 600)
        glVertex2f(760, 600)
        glVertex2f(760, 0)
        glEnd()

        #piedras
        
        alturas = np.linspace(50, 550, 15)
        for h in alturas:
            glBegin(GL_TRIANGLE_FAN)
            glColor3f(192 / 255.0, 192 / 255.0, 192 / 255.0)  
            glVertex2f(20, h)
            radio1 = 10
            ang = 2 * pi / 20
            for i in range(20):
                ang_i = ang * i
                glVertex2f(20+cos(ang_i) * radio1, h+sin(ang_i) * radio1)
            glVertex2f(20 + radio1, h)
            glEnd()
            
            glBegin(GL_TRIANGLE_FAN)
            glColor3f(192 / 255.0, 192 / 255.0, 192 / 255.0)  
            glVertex2f(780, h)
            ang = 2 * pi / 20
            for i in range(20):
                ang_i = ang * i
                glVertex2f(780 + cos(ang_i) * radio1, h +sin(ang_i) * radio1)
            glVertex2f(780 + radio1, h)
            glEnd()
        alturas2 = np.linspace(45, 565, 15)
        for h in alturas2:
            glBegin(GL_TRIANGLE_FAN)
            glColor3f(119 / 255.0, 139 / 255.0, 153 / 255.0)  
            glVertex2f(15, h)
            radio1 = 8
            ang = 2 * pi / 20
            for i in range(20):
                ang_i = ang * i
                glVertex2f(15 + cos(ang_i) * radio1, h + sin(ang_i) * radio1)
            glVertex2f(15 + radio1, h)
            glEnd()
            glBegin(GL_TRIANGLE_FAN)
            glColor3f(119 / 255.0, 139 / 255.0, 153 / 255.0)  
            glVertex2f(785, h)
            radio1 = 8
            ang = 2 * pi / 20
            for i in range(20):
                ang_i = ang * i
                glVertex2f(785 + cos(ang_i) * radio1, h + sin(ang_i) * radio1)
            glVertex2f(785 + radio1, h)
            glEnd()
        alturas3 = np.linspace(1, 501, 15)
        for h in alturas2:
            glBegin(GL_TRIANGLE_FAN)
            glColor3f(0 / 255.0, 0 / 255.0, 0 / 255.0)  
            glVertex2f(25, h)
            radio1 = 5
            ang = 2 * pi / 20
            for i in range(20):
                ang_i = ang * i
                glVertex2f(25 + cos(ang_i) * radio1, h + sin(ang_i) * radio1)
            glVertex2f(25 + radio1, h)
            glEnd()
            glBegin(GL_TRIANGLE_FAN)
            glColor3f(0 / 255.0, 0 / 255.0, 0 / 255.0)  
            glVertex2f(775, h)
            radio1 = 5
            ang = 2 * pi / 20
            for i in range(20):
                ang_i = ang * i
                glVertex2f(775 + cos(ang_i) * radio1, h + sin(ang_i) * radio1)
            glVertex2f(775 + radio1, h)
            glEnd()
