class Players(object):

    def __init__(self,Name,Money,Position):
        self.Name = Name
        self.Money = int(Money)
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

