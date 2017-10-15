#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 22:30:38 2017

@author: terevaldivia
"""

import os
from CC3501Utils_personal import *


class PlataformaLiana(Figura):
    ancho = 200
    
    def __init__(self, pos=Vector(0, 0), rgb=(1.0, 1.0, 1.0)):
        super(PlataformaLiana, self).__init__(pos, rgb)
    
    def figura(self):
        #cuerpo
        glBegin(GL_QUADS)
        glColor3f(50 / 255.0, 205 / 255.0, 50 / 255.0) #Verde
        glVertex2f(-self.ancho/2, 0)  
        glVertex2f(-self.ancho/2, -25)  
        glVertex2f(self.ancho/2, -25)
        glVertex2f(self.ancho/2, 0)  
        glEnd()
        #hoja izquierda
        glBegin(GL_QUADS)
        glColor3f(50 / 255.0, 205 / 255.0, 50 / 255.0)
        glVertex2f(-self.ancho/2, -12)
        glVertex2f(-(self.ancho/2+15), 0)
        glVertex2f(-(self.ancho/2+30), -12)
        glVertex2f(-(self.ancho/2+15), -25)
        glEnd()
        #hoja derecha
        glBegin(GL_QUADS)
        glColor3f(50 / 255.0, 205 / 255.0, 50 / 255.0)
        glVertex2f(self.ancho/2, -12)
        glVertex2f((self.ancho/2+15), 0)
        glVertex2f((self.ancho/2+30), -12)
        glVertex2f((self.ancho/2+15), -25)
        glEnd()
        
    def update(self, camara):
        self.pos.y -= camara.y
        pass
        
        
class PlataformaPiedra(Figura):
    
    ancho = 200
    def __init__(self, pos=Vector(0, 0), rgb=(1.0, 1.0, 1.0)):
        super(PlataformaPiedra, self).__init__(pos, rgb)
    
    def figura(self):
        #cuerpo
        glBegin(GL_QUADS)
        glColor3f(220 / 255.0, 220 / 255.0, 220 / 255.0) #Gris
        glVertex2f(-self.ancho/2, 0)  
        glVertex2f(-(self.ancho/2-20), -25)  
        glVertex2f(self.ancho/2-20, -25)
        glVertex2f(100, 0)  
        glEnd()
        glBegin(GL_QUADS)
        glColor3f(105 / 255.0, 105 / 255.0, 105 / 255.0) #Gris
        glVertex2f(-self.ancho/2, 0)  
        glVertex2f(-(self.ancho/2-10), -12.5)  
        glVertex2f(self.ancho/2-10, -12.5)
        glVertex2f(self.ancho/2, 0)  
        glEnd()
        glBegin(GL_QUADS)
        glColor3f(47 / 255.0, 79 / 255.0, 79 / 255.0) #Gris
        glVertex2f(-10, 0)  
        glVertex2f(-10, -20)  
        glVertex2f(10, -20)
        glVertex2f(10, 0)  
        glEnd()
        glBegin(GL_QUADS)
        glColor3f(47 / 255.0, 79 / 255.0, 79 / 255.0) #Gris
        glVertex2f(-50, 0)  
        glVertex2f(-50, -20)  
        glVertex2f(-40, -20)
        glVertex2f(-40, 0)  
        glEnd()
        glBegin(GL_QUADS)
        glVertex2f(40, 0)  
        glVertex2f(40, -20)  
        glVertex2f(50, -20)
        glVertex2f(50, 0)  
        glEnd()
        
    def update(self, camara):
        self.pos.y -= camara.y
        pass
        
class PlataformaMadera(Figura):
    ancho = 200
    def __init__(self, pos=Vector(0, 0), rgb=(1.0, 1.0, 1.0)):
        super(PlataformaMadera, self).__init__(pos, rgb)
    
    def figura(self):
        #cuerpo
        glBegin(GL_QUADS)
        glColor3f(165 / 255.0, 42 / 255.0, 42 / 255.0) #cafe
        glVertex2f(-self.ancho/2, 0)  
        glVertex2f(-self.ancho/2, -25)  
        glVertex2f(self.ancho/2, -25)
        glVertex2f(self.ancho/2, 0)  
        glEnd()
        glBegin(GL_QUADS)
        glColor3f(160 / 255.0, 82 / 255.0, 45 / 255.0) 
        glVertex2f(-self.ancho/2, -10)  
        glVertex2f(-self.ancho/2, -20)  
        glVertex2f(self.ancho/2, -20)
        glVertex2f(self.ancho/2, -10)  
        glEnd()
        glBegin(GL_QUADS)
        glColor3f(205 / 255.0, 133 / 255.0, 63 / 255.0) 
        glVertex2f(-self.ancho/2, 0)  
        glVertex2f(-self.ancho/2, -10)  
        glVertex2f(self.ancho/2, -10)
        glVertex2f(self.ancho/2, 0)  
        glEnd()
    
    def update(self, camara):
        self.pos.y -= camara.y
        pass