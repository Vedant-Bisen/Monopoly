from Players import *
from Properties import *
from Board import *

PlayOrder = []
PlOrder = 0
def Start():
    i = int(input("How many players wish to play: "))
    for i in range(0,i):
        Name = input("Enter the Name of player: ")
        Name = Players(Name,5000,0)
        PlayOrder.append(Name)
        print(PlayOrder)

def Play():
    print("Order of moving is: ")
    for i in range(0,len(PlayOrder)):
        print(PlayOrder[i].Call_Name())
    





Start()
Play()
