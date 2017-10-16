#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  8 12:59:18 2017

@author: terevaldivia

Escena inicial
"""

import os
from CC3501Utils_personal import *

from Plataforma import *
from Reloj import *
from Muros import *
from Jugador import *
from Fondo import *
from Camara import *

def main():
    ancho = 800
    alto = 600
    init(ancho, alto, "titulo")

    p = Jugador(Vector(180 + 12, 50 + 70))
    r = Reloj(Vector(50,450))
    fondo = Fondo(Vector(0,0))
    camara = Camara(p)
    piedra = PlataformaPiedra(Vector(200, 50))
    liana = PlataformaLiana(Vector(400, 150))  
    madera = PlataformaMadera(Vector(650, 250))
    liana2 = PlataformaLiana(Vector(500, 400))
    piedra2 = PlataformaPiedra(Vector(200, 500))
    muro = Muros(Vector(0,0))
    
    elementos = [fondo, piedra, liana, madera, liana2, piedra2, muro, p, r]
    plataformas = [piedra, liana, madera, liana2, piedra2]
    run = True
    
    while run:
        pygame.event.pump()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # cerrar ventana
                run = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pass
                if event.key == pygame.K_RIGHT:
                    p.pos += Vector(20, 0)
                if event.key == pygame.K_LEFT:
                    p.pos -= Vector(20, 0)
                if event.key == pygame.K_UP:
                    p.pos += Vector(0, 20)
                if event.key == pygame.K_DOWN:
                    p.pos -= Vector(0, 20)
                    
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)  # limpiar buffers

        # dibujar figuras
        
        p.update(plataformas, camara)
        r.update(fps)
        for elem in elementos:
            elem.dibujar()
        

        pygame.display.flip()  # actualizar pantalla
        clock.tick(fps)
        
    pygame.quit()


main()