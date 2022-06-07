from Players import *
from Properties import *
from random import randint


def throw(Player,Dice):
    Dice = randint(0,12)
    move(Player,Dice)

def move(Player,Dice):
    Player.Position += Dice


def buy(Player,Property):
    if Players.Call_Money(Player)>Properties.Call_Price(Property):
        Player.Money -= Property.Price
        Property.Owner = str(Player)
        Player.Props.append(Properties.Call_Name(Property))
        Property.Owner = Players.Call_Name(Player)
        print(Properties.Call_Name(Property),"bought by",Players.Call_Name(Player))
    else:
        print(Players.Call_Name(Player),"does not have enough money to buy ",Properties.Call_Name(Property))


