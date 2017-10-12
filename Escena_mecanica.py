#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  8 13:49:35 2017

@author: terevaldivia

Escena Mecánica
"""

import os
from CC3501Utils_personal import *

from Plataforma import *
from Reloj import *
from Muros import *
from Jugador import *

def main():
    ancho = 800
    alto = 600
    init(ancho, alto, "titulo")

    p = Jugador(Vector(180 + 12, 50 + 70))
    r = Reloj(Vector(50,450))
    piedra = PlataformaPiedra(Vector(200, 50))
    liana = PlataformaLiana(Vector(400, 150))  
    madera = PlataformaMadera(Vector(650, 250))
    liana2 = PlataformaLiana(Vector(500, 400))
    piedra2 = PlataformaPiedra(Vector(200, 500))
    muro = Muros(Vector(0,0))
    
    elementos = [piedra, liana, madera, liana2, piedra2, muro, p, r]
    plataformas = [piedra, liana, madera, liana2, piedra2]
    run = True
    
    while run:
        pygame.event.pump()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # cerrar ventana
                run = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    p.vel_y += 20
                if event.key == pygame.K_RIGHT:
                    p.vel_x += 20
                    if p.vel_x > p.max_vel_x:
                        p.vel_x = p.max_vel_x
                if event.key == pygame.K_LEFT:
                    p.vel_x = -20
                    if p.vel_x < -p.max_vel_x:
                        p.vel_x = -p.max_vel_x
         
            
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)  # limpiar buffers

        # dibujar figuras
        
        p.update(plataformas)
        r.update(fps)
        for elem in elementos:
            elem.dibujar()
        

        pygame.display.flip()  # actualizar pantalla
        clock.tick(fps)
        
    pygame.quit()


main()
