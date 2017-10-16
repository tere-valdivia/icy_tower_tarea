#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 20:11:06 2017

@author: terevaldivia
"""
import os
from CC3501Utils_personal import *
from Plataforma import *
from Muros import *

os.environ['SDL_VIDEO_CENTERED'] = '1'  # centrar pantalla

class Jugador(Figura):
    vel_x = 0
    vel_y = 0
    
    ac_y = 1 #gravedad
    ac_x = 0.5
    max_vel_y = -10
    max_vel_x = 10
    
    def __init__(self, pos=Vector(0, 0), rgb=(1.0, 1.0, 1.0)):
        super(Jugador, self).__init__(pos, rgb)
    
    def figura(self):
        #queremos hacer un pescado
        
        #empezamos por el cuerpo
        glBegin(GL_QUADS)
        glColor3f(66 / 255.0, 226 / 255.0, 244 / 255.0) #celeste
        glVertex2f(12, -15)  
        glVertex2f(-12, -15)  
        glVertex2f(-12, -50)
        glVertex2f(12, -50)  
        glEnd()
        
        #seguimos con la cabeza        
        glBegin(GL_TRIANGLES) 
        glColor3f(66 / 255.0, 226 / 255.0, 244 / 255.0)
        glVertex2f(12, -15)
        glVertex2f(-12, -15) #los dos extremos superiores del tronco
        glVertex2f(0, 8) #y la punta superior
        glEnd()
        
        #ahora vamos por las aletas
        glBegin(GL_TRIANGLES)
        glColor3f(66 / 255.0, 226 / 255.0, 244 / 255.0) # azul
        # pierna1
        glVertex2f(-12, -50)  # cadera
        glVertex2f(0, -50)
        glVertex2f(-6, -70)
        
        glVertex2f(12, -50)  # cadera
        glVertex2f(0, -50)
        glVertex2f(6, -70)
        glEnd()
        
        #y terminamos con un bello ojo
        
        glBegin(GL_QUADS)
        glColor3f(0.0, 0.0, 0.6)
        glVertex2f(-5, -10)
        glVertex2f(-5, -14)
        glVertex2f(-1, -14)
        glVertex2f(-1, -10)
        
        glEnd()

        
        
    def update(self, platformList, camara):
        self.pos += Vector(self.vel_x, self.vel_y - camara.y)
        self.ac_y = 1#reseteo fuera de la plataforma
        self.vel_y -= self.ac_y
        #control muros
        if self.pos.x + 12 >= 760:
            self.pos.x = 760 - 12
            self.vel_x = -self.vel_x
            
        if self.pos.x - 12 <= 40:
            self.pos.x = 40 + 12
            self.vel_x = -self.vel_x
        
        #aceleracion en eje x
        if self.vel_x > 0:
            self.vel_x -= self.ac_x
        elif self.vel_x < 0:
            self.vel_x += self.ac_x
            
        #aceleracion en eje y
        if self.vel_y <= self.max_vel_y:
            self.vel_y = self.max_vel_y
        if self.vel_y <= 0 and self.estaSobreAlgunaPlataforma(platformList):
            self.vel_y = 0
            self.ac_y = 0
    
        else: self.vel_y -= self.ac_y
        
        #fin de camara
        if self.fueraDePantalla(camara):
            self.vel_y = 0
            self.ac_y = 0
        
        
    
    def estaSobrePlataforma(self, plataforma):
        #plataforma es un objeto tipo Plataforma
        sobre = (self.pos.y - 60 < plataforma.pos.y) and (self.pos.y - 60 > plataforma.pos.y - 20)
        izq = self.pos.x >= plataforma.pos.x - plataforma.ancho/2
        der = self.pos.x <= plataforma.pos.x + plataforma.ancho/2
        return sobre and izq and der
    
    def estaSobreAlgunaPlataforma(self, platformList):
        for plataforma in platformList:
            if self.estaSobrePlataforma(plataforma): return True
        return False
    
    def fueraDePantalla(self, camara):
        return (self.pos.y - camara.y + 70) <=70
    
    def is_jumping(self):
        return self.vel_y>0 or self.vel_y<0
    
        
    