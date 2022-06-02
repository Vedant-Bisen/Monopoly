from Players import *
from Properties import *

def move(Player,Dice):
    

def buy(Player,Property):
    if Players.Call_Money(Player)>Properties.Call_Price(Property):
        Player.Money -= Property.Price
        Property.Owner = str(Player)
        Player.Props.append(Properties.Call_Name(Property))
        Property.Owner = Players.Call_Name(Player)
        print(Properties.Call_Name(Property),"bought by",Players.Call_Name(Player))
    else:
        print(Players.Call_Name(Player),"does not have enough money to buy ",Properties.Call_Name(Property))

vedant = Players("Vedant",1000,0)
Old_Kent = Properties("OldKent",2000,0)

#buy(vedant,Old_Kent)
