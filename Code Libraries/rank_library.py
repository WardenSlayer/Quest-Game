# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 21:37:31 2020

@author: Ben Loll

Questar Document 4
    
This program is intended to be imported by other files

Rank Library
"""
class ranks:
    def __init__(self,m = 0, t = "none", i = 'none', s = 0):
        self.id = m #internal rank ID
        self.title = t #rank title (ie squire)
        self.image = i #rank image for display
        self.stats = s #rank strength (5,10,20)

#Create Ranks
squire = ranks(1,"Squire", 'image_placeholder', 5)
knight = ranks(2,"Knight", 'image_placeholder', 10)
champion = ranks(3,"Champion", 'image_placeholder', 20)