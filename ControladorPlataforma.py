#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 14 15:26:23 2017

@author: terevaldivia
"""
import os
from CC3501Utils_personal import *
import numpy as np
from Plataforma import *

class ControladorPlataforma:
    def __init__(self):
        self.lista = []
        self.generar()
    
    def generar(self):
        #20 plataformas de piedra
        alturas = np.linspace(150, 2100, 19)
        mu = 400
        sigma = 100
        self.lista.append(PlataformaPiedra(Vector(180 + 12, 50)))
        for a in alturas:
            new = PlataformaPiedra(Vector(np.random.normal(loc=mu, scale=sigma), a))
            self.lista.append(new)
        #20 de liana
        alturas +=2050
        for a in alturas:
            new = PlataformaLiana(Vector(np.random.normal(loc=mu, scale=sigma), a))
            self.lista.append(new)
        #y 10 de madera
        alturas += 2050
        for a in alturas:
            new = PlataformaMadera(Vector(np.random.normal(loc=mu, scale=sigma), a))
            self.lista.append(new)
        