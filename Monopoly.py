'''Create dictionaries for each property
    '''
import random

class OldKent:
  pos = 1
  price = 60
  #"owner": ""
  houses = 0

class WhiteChapal:
  pos = 2
  price = 60
  #"owner": ""
  houses = 0

class KingsCross:
  pos = 3
  price = 60
  #"owner": ""
  houses = 0

class TheAngel:
  pos = 4
  price = 100
  #"owner": "",
  houses = 0

class EustonRoad:
  pos = 5
  price = 60
  #"owner": ""
  houses = 0

class PentonVille:
  pos = 6
  price = 60
  #"owner": ""
  houses = 0


players = []
places = [OldKent,WhiteChapal,KingsCross,TheAngel,EustonRoad,PentonVille]



def initial():
    n = int(input("Enter the total number of players in playing order: "))
    for i in range(0,n):
        name = input("Enter the name of player: ")
        class name:
          pos = 0
          money = 5000
        players.append(name)
   

def dice_roll():
    rand = random.randint(0,2)
    return rand
  
#def buy(player[i],places):


initial()