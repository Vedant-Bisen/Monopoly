from Monopoly.Properties import Properties


class Players(object):

    def __init__(self,Name,Money,Position,Props):
        self.Name = Name
        self.Money = Money
        self.Position = Position
        self.Props = []
    
    def Call_Name(self):
        return self.Name

    def Call_Money(self):
        return self.Money

    def Call_Position(self):
        return self.Position

    def Call_Props(self):
        return self.Props

    def Buy(self):
        if Players.Call_Money <= Properties.Call_Price:
            self.Props.append(Properties.Call_Name)
        else:
            print("Ya POOR")

    def House()