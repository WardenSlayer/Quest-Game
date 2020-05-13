# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 21:37:31 2019

@author: Ben Loll

Questar Document 3

This program is intended to be imported by other files

Player Library
"""
import random
titles = ["Waldo the Walrus", "Greg the Giraffe",
          "Arthur the Aardvark", "Leroy the Lemming"]

def initialize_Player(num):
    #Creates a new player
    #Arg is a player number
    global titles
    name = random.choice(titles)
    titles.remove(name)
    pl = player(num,name)
    #returns player object
    return pl

class player:
    def __init__(self, m = 0, n = 'placeholder', r = "Squire", s = 0, h = [], c = "false",
                 a = 'placeholder',g = 0,b = 0,z = "false",y = "false",x = "false",
                 w = "false",v = "false",u = "false",t = "false"):
        self.number = m #player number (ID)
        self.name = n #player name
        self.rank = r #current rank
        self.shields = s #current shield count
        self.hand = h #cards in hand
        self.victory = c #has this player won (boolean)
        self.allies = a #in play allies
        self.allyStr = g #total strength from in play allies
        self.allyBid = b #total bids from in play allies
        #equipment below (boolean value: true if equiped else false)
        self.dag = z
        self.sword = y
        self.amour = x
        self.horse = w
        self.axe = v
        self.lance = u
        self.excalibur = t

def levelUp(player,shields):
    #Awards a player with shields and checks for a level up or win
    #Args player number and num shields won
    rank = player.rank
    currentShields = player.shields
    victory = player.victory
    netShields = currentShields+shields
    newRank = ""
    if rank == 'Squire' and netShields < 5:
        newRank = rank
    elif rank == 'Squire' and netShields >= 5:
        newRank = 'Knight'
        netShields = netShields-5
    elif rank == 'Knight' and netShields < 7:
        newRank = 'Knight'
    elif rank == 'Knight' and netShields >= 7:
        newRank = 'Champion'
        netShields = netShields-7
    elif rank == 'Champion' and netShields < 10:
        newRank = 'Champion'
    elif rank == 'Champion' and netShields >= 10:
        newRank = 'Knight of the Round Table'
        victory = 'true'
    player.rank = newRank
    player.shields = netShields
    #Set the victory flag to end game
    player.victory = victory
    if rank != newRank and player.victory != 'true':
        print(player.name+" has leveled up to "+player.rank)
        #Check for a double level up (rare but best to account for it)
        levelUp(player,netShields)
    #return unimportant
    print("levelUp successful")
