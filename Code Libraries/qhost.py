### -*- coding: utf-8 -*-
"""
Created on Tue Jun  2 17:27:58 2020

@author: Jordan Loll

Questar Document 6

Hosting Option

Description:
    Quest hosting
    takes in a quest card
    check if player is able to host (stages, foes, test, etc)
    confirm hosting or passing 
"""

### imports
from AD import Adventure_Deck
from SD import Story_Deck
import player_library
import random #for testing

### quick reference variables
sd = Story_Deck
ad = Adventure_Deck






### pick a random quest from the SD --- active quest = 'aq'
qts = []
for i in sd:
    if sd[i].type == 'quest':
        qts.append(sd[i])


for n in range(0,1): # 1 random quest cart from qts
    random_key = random.sample(list(qts), 1)[0]
    aq = random_key
    print(aq.title, "has", aq.stages, "stages.")







### temproary player hand
pl = player_library.initialize_Player(1)
#print(pl.name)
print()

for n in range(0,10): # 10 random cards for test hand
    random_key = random.sample(list(Adventure_Deck), 1)[0]
    pl.hand.append(Adventure_Deck[random_key])








### function to check for number of foes and tests in players hand and return if hosting is possible

def CanHost(playerhand, quest):
    foes = 0
    tests = 0
    host = False
    
    # count foes and tests in player hand
    for i in playerhand:
        if i.type == 'foe':
            foes += 1
        if i.type == 'test':
            tests += 1
    
    
    # check if player has enough foes/tests for the require stages of the quest
    if tests != 0:
        if quest.stages - 1 > foes:
            print("Cannot Host")
        else:
            print('can host')
            host = True
    else:
        if quest.stages > foes:
            print("cannot Host")
        else:
            print('can host')
            host = True
            
    return(host)




### display decision

print(pl.name)
result = CanHost(pl.hand, aq)
print(aq.title)


#print(result)







