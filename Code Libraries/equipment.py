# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 12:35:48 2020

@author: jordan loll

Equipment Structure

Takes in a base (player or foes)
Takes in Hand

Gives options for possible equipment

Players has choice and can change aound equipment then confirms

outputs total battle points
"""
from AD import Adventure_Deck
from SD import Story_Deck
import player_library
from rank_library import squire
from rank_library import knight
from rank_library import champion


""" temporary player and hand  to be removed """
import random
pl = player_library.initialize_Player(1)
print(pl.name)
print()

for n in range(0,10): # 10 random cards for test hand
    random_key = random.sample(list(Adventure_Deck), 1)[0]
    #print(random_key)
    pl.hand.append(Adventure_Deck[random_key])

#print("Hand:")
#for i in pl.hand:
#    print(i.title)



"""input player hand, output unique equipable options"""
def eqOptions(hand):
    equipable = []
    # find weapon and amour cards
    for i in hand:
        if i.type == 'amour' or  i.type == 'weapon':
            equipable.append(i)
    
    # if they are unique, add them to options based on title
    options = []
    for i in equipable:
        if i.title not in options:
            options.append(i)
            options.append(i.title)
    
    # remove the string titles leaving just the card objects in options
    for i in options:
        if isinstance(i, str) == True:
            options.remove(i)
            
    return(options)


#Check for eqOptions functionality      
print()
#print("Options:")
opt = eqOptions(pl.hand)
#for i in opt:
    #print(i.title)

print()


"""player process of equipment and confirmation + battle points calc"""
def equipPlayer(options, player):
    bps = 0
    if player.rank == "Squire":
        bps += 5
    elif player.rank == "Knight":
        bps += 10
    elif player.rank == "Champion":
        bps += 20
    elif player.rank != "Squire" or "Knight" or "Champion":
        print("Error, must be a player rank as a string")
        return
    
    # player (de)equips options until battle points are confirmed
    equipped = []
    done = 'no'
    while done != 'yes':
        
        #current display
        print()
        print("Your current battles points: ", bps)
        confirm = str(input("Would you like to add equipment, remove equipment, or finish? [add/remove/finish] "))

        viable = False
        
        
        # Adding Equipment Code
        
        if confirm == 'add':
            if len(options) == 0:
                print("No more equippable cards")
            else:
                
                print()
                print("Please select a weapon from the following options:")
                for i in options:
                    if i not in equipped:
                        print(i.title)
                eq = str(input("select weapon: "))
                
                for j in options:
                    if j.title == eq:
                        bps += j.stats
                        equipped.append(j)
                        options.remove(j)
                        viable = True
                
                if viable == False:
                    print("No card(s) equipped")
                else:
                    print("Equipped Cards: ")
                    for n in equipped:
                        print(n.title)
        
       # Removing Equipment Code 
        
        
        elif confirm == 'remove':
            if len(equipped) == 0:
                print("No card currently equipped.")
            else:
                print("Currently Equipped:")
                for i in equipped:
                    print(i.title)
                deq = str(input("select weapon: "))
            
                for j in equipped:
                    if j.title == deq:
                        bps -= j.stats
                        options.append(j)
                        equipped.remove(j)
                        viable = True
                
                if viable == False:
                    print("No card(s) de-equipped")
                else:
                    print("Equipped Cards: ")
                    for n in equipped:
                        print(n.title)
        
        
        # confirm and exit / error handling
    
        elif confirm == 'finish':
            print()
            done = input("Confirm selections [yes/no]: ")
        else:
            print("Error: please choose 'add' 'remove' or 'finish'")
        
        
        
        
        
        
        
    print()    
    print(str(player.rank)+" is equipped with:")
    for i in equipped:
        print(i.title)
    print("Final Battle Points: ", bps)


#equipPlayer(opt, pl)   
    


   

"""Foe process of equipment and confirmation + battle points calc"""

def equipFoe(options, foe):
    bps = 0
    bps += foe.stats[0] # [1] if it is foes quest!
    
    # player (de)equips options until battle points are confirmed
    equipped = []
    done = 'no'
    while done != 'yes':
        
        #current display
        print()
        print("Your current battles points: ", bps)
        confirm = str(input("Would you like to add equipment, remove equipment, or finish? [add/remove/finish] "))
        
        #equipped = [] #### THIS ZEROS OUT EQUIPMENT CHOICES EVERY LOOP = PROBLEM ###
        viable = False
        
        
        # Adding Equipment Code
        
        if confirm == 'add':
            if len(options) == 0:
                print("No more equippable cards")
            else:
                print()
                print("Please select a weapon from the following options:")
                for i in options:
                    if i not in equipped:
                        print(i.title)
                eq = str(input("select weapon: "))
                
                for j in options:
                    if j.title == eq:
                        bps += j.stats
                        equipped.append(j)
                        options.remove(j)
                        viable = True
                
                if viable == False:
                    print("No card(s) equipped")
                else:
                    print("Equipped Cards: ")
                    for n in equipped:
                        print(n.title)
        
       # Removing Equipment Code 
        
        
        elif confirm == 'remove':
            if len(equipped) == 0:
                print("No card currently equipped.")
            else:
                print("Currently Equipped:")
                for i in equipped:
                    print(i.title)
                deq = str(input("select weapon: "))
            
                for j in equipped:
                    if j.title == deq:
                        bps -= j.stats
                        options.append(j)
                        equipped.remove(j)
                        viable = True
                
                if viable == False:
                    print("No card(s) de-equipped")
                else:
                    print("Equipped Cards: ")
                    for n in equipped:
                        print(n.title)
        
        
        # confirm and exit / error handling
    
        elif confirm == 'finish':
            print()
            done = input("Confirm selections [yes/no]: ")
        else:
            print("Error: please choose 'add' 'remove' or 'finish'")


        print()    
        print(foe.title +" is equipped with:")
        for i in equipped:
            print(i.title)
        print("Final Battle Points: ", bps)
        

### take one foe from deck
bane = Adventure_Deck['bknight1']
print(bane.title, type(bane.stats[0]))
### function check
equipFoe(opt, bane)