#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 22:30:38 2017

@author: terevaldivia
"""

import os
from CC3501Utils import *

class Plataforma(Figura):
    
    def __init__(self, pos=Vector(0, 0), rgb=(1.0, 1.0, 1.0)):
        super().__init__(pos, rgb)
    
    def figura(self):
        
        
        