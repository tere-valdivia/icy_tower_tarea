#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 20:11:06 2017

@author: terevaldivia
"""
import os
from CC3501Utils_personal import *
from Plataforma import *
from Reloj import *
import numpy as np

os.environ['SDL_VIDEO_CENTERED'] = '1'  # centrar pantalla
fps = 60
clock = pygame.time.Clock()

class Jugador(Figura):
    vel_x = 0
    vel_y = 0
    max_vel_caida = -20
    ac_salto = 50
    ac_gravedad = 10
    
    aceleracion = 0.5
    max_vel_x = 8
    
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

        
    def update(self):
        self.pos += Vector(self.vel_x, self.vel_y)
        if self.vel_x > 0:
            new_x = self.vel_x -self.aceleracion
            self.vel_x = 0 if new_x < 0 else new_x
        elif self.vel_x < 0:
            new_x = self.vel_x +self.aceleracion
            self.vel_x = 0 if new_x > 0 else new_x
        
        pass
        
        

def main():
    ancho = 800
    alto = 600
    init(ancho, alto, "titulo")

    p = Jugador(Vector(400, 300))
    
    r = Reloj(Vector(200,200))
    
    
    run = True
    
    while run:
        pygame.event.pump()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # cerrar ventana
                run = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pass
                if event.key == pygame.K_w:
                    p.pos += Vector(0, 20)
                if event.key == pygame.K_RIGHT:
                    p.vel_x += 10 * p.aceleracion
                    if p.vel_x == p.max_vel_x:
                        p.vel_x = p.max_vel_x
                if event.key == pygame.K_LEFT:
                    p.vel_x -= 10 * p.aceleracion
                    if p.vel_x == -p.max_vel_x:
                        p.vel_x = -p.max_vel_x
                if event.key == pygame.K_UP:
                    if p.vel_y == 0: p.vel_y += p.ac_salto
                if event.key == pygame.K_DOWN:
                    p.pos -= Vector(0, 20)
                    
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)  # limpiar buffers

        # dibujar figuras
        
        p.update()
        r.update(fps)
        p.dibujar()
        r.dibujar()
        print r.x_palito, r.y_palito, r.segundo

        pygame.display.flip()  # actualizar pantalla
        clock.tick(fps)
        
    pygame.quit()


main()