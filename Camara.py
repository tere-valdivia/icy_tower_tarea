#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 13:15:14 2017

@author: terevaldivia
"""

import os
from CC3501Utils_personal import *
import numpy as np

class Camara:
    def __init__(self, player):
		self.y = 0
		self.player = player
        
    def update(self):
        if self.player.pos.y - self.y >= 600./2:
            self.y = self.player.pos.y - 600./2
        else: 
            self.y = 0