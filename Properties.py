
from Monopoly.Players import Players


class Properties(object):

    def __init__(self,Name,Price,Position,Houses,Owner):
        self.Name = Name
        self.Price = Price
        self.Position = Position
        self.Houses = 0
        self.Owner = ""
    
    def Call_Name(self):
        return self.Name

    def Call_Price(self):
        return self.Price

    def Call_Position(self):
        return self.Position

    def Call_Price(self):
        return self.Price
    
    def Bought(self):
        self.Owner = Players.Call_Name
        pass


    