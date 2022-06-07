from Players import *
from Properties import *
from Board import *

def Play():
    PlayOrder = []
    i = int(input("How many players wish to play: "))
    for i in range(0,i):
        Name = input("Enter the Name of player: ")
        Name = Players(Name,5000,0)
        PlayOrder.append(Name)
        print(PlayOrder)
    







Play()
