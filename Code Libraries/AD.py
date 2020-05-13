# -*- coding: utf-8 -*-
"""
Created on Thu Jan  2 15:44:00 2020

@author: jordan loll

Questar Document 1
    
This program is intended to be imported by other files

Adventure Deck
    49 weapons
    50 Foes
    8 Tests
    10 Allies
    8 Amours


"""
Adventure_Deck = {}


""" Weapons"""
class weapon:
    def __init__(self, t = "none", y = "none", s = 0):
        self.title = t
        self.type = y
        self.stats = s

# 2 Excalibur
for i in range(1,3):
    Adventure_Deck["excalibur{0}".format(i)]= weapon("Excalibur", 'weapon', 30)
# 6 Lance
for i in range(1,7):
    Adventure_Deck["lance{0}".format(i)]= weapon("Lance", 'weapon', 20)
# 8 Battle Axes
for i in range(1,9):
    Adventure_Deck["axe{0}".format(i)]= weapon("Battle Axe", 'weapon', 15)
# 16 Sword
for i in range(1,17):
    Adventure_Deck["sword{0}".format(i)]= weapon("Sword", 'weapon', 10)
# 11 Horse
for i in range(1,12):
    Adventure_Deck["horse{0}".format(i)]= weapon("Horse", 'weapon', 10)
# 6 Dagger
for i in range(1,7):
    Adventure_Deck["dagger{0}".format(i)]= weapon("Dagger", 'weapon', 5)


"""Foes"""
class foe:
    def __init__(self, t = "none", y = 'none', s = 0):
        self.title = t
        self.type = y
        self.stats = s

# 1 Dragon
for i in range(1,2):
    Adventure_Deck["dragon{0}".format(i)]=  foe("Dragon",        'foe', (50,70))
# 2 Giant
for i in range(1,3):
    Adventure_Deck["giant{0}".format(i)]=   foe("Giant",         'foe', (40,40))
# 4 Mordred
for i in range(1,5):
    Adventure_Deck["mordred{0}".format(i)]= foe("Mordred",       'foe', (30,30))
# 2 Green Knight
for i in range(1,3):
    Adventure_Deck["gknight{0}".format(i)]= foe("Green Knight",  'foe', (25,40))
# 3 Black Knight
for i in range(1,4):
    Adventure_Deck["bknight{0}".format(i)]= foe("Black Knight",  'foe', (25,35))
# 6 Evil Knight
for i in range(1,7):
    Adventure_Deck["eknight{0}".format(i)]= foe("Evil Knight",   'foe', (20,30))
# 8 Saxon Knight
for i in range(1,9):
    Adventure_Deck["sknight{0}".format(i)]= foe("Saxon Knight",  'foe', (15,25))
# 7 Robber Knight
for i in range(1,8):
    Adventure_Deck["rknight{0}".format(i)]= foe("Robber Knight", 'foe', (15,15))
# 5 Saxons
for i in range(1,6):
    Adventure_Deck["saxon{0}".format(i)]=   foe("Saxons",        'foe', (10,20))
# 4 Boar
for i in range(1,5):
    Adventure_Deck["boar{0}".format(i)]=    foe("Boar",          'foe', (5,15))
# 8 thieves
for i in range(1,9):
    Adventure_Deck["thieves{0}".format(i)]= foe("Thieves",       'foe', (5,5))


"""Allies"""
class ally:
    def __init__(self, t = "none", y = 'none', s = 0, e = 'none'):
        self.title = t
        self.type = y
        self.stats = s
        self.effect = e

Adventure_Deck["ally1"]= ally("Sir Galahad",     'ally', 15)
Adventure_Deck["ally2"]= ally("Sir Lancelot",    'ally', 15, "+25 on the Quest, Defend the Queen's Honor.")
Adventure_Deck["ally3"]= ally("King Arthur",     'ally', 10, "2 bids")
Adventure_Deck["ally4"]= ally("Sir Tristan",     'ally', 10, "+20 when Queen Insuelt is in play")
Adventure_Deck["ally5"]= ally("King Pellinore",  'ally', 10, "4 bids on the Quest, the Search for the Questing Beast")
Adventure_Deck["ally6"]= ally("Sir Gawain",      'ally', 10, "+20 on the Quest, The Test of the Green Knight")
Adventure_Deck["ally7"]= ally("Sir Percival",    'ally', 5, "+20 on the Quest, The Search for the Holy Grail")
Adventure_Deck["ally8"]= ally("Queen Guinevere", 'ally', 0, "3 bids")
Adventure_Deck["ally9"]= ally("Queen Insuelt",   'ally', 0, "2 bids, 4 bids when Sir Tristan is in play")
Adventure_Deck["ally10"]= ally("Merlin",         'ally', 0, "Preview one stage per quest")


"""Tests"""
class test:
    def __init__(self, t = "none", y = "none", bm = (0,0)):
        self.title = t
        self.type = y
        self.bid_minimum = bm

Adventure_Deck["test1"]= test("Test of Valor",              "test")
Adventure_Deck["test2"]= test("Test of Valor",              "test")
Adventure_Deck["test3"]= test("Test of the Questing Beast", "test", (0,4))
Adventure_Deck["test4"]= test("Test of the Questing Beast", "test", (0,4))
Adventure_Deck["test5"]= test("Test of Temptation",         "test")
Adventure_Deck["test6"]= test("Test of Temptation",         "test")
Adventure_Deck["test7"]= test("Test of Morgan Le Fey",      "test", (3,3))
Adventure_Deck["test8"]= test("Test of Morgan Le Fey",      "test", (3,3))


"""Amours"""
class amour:
    def __init__(self, t = "Amour", y= 'amour', bp = 10, d = 1):
        self.title = t
        self.type = y
        self.stats = bp
        self.bid = d

for i in range(1,9):
    Adventure_Deck["amour{0}".format(i)]= amour()