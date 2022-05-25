from Players import *
from Properties import *


vedant = Players("vedant",1000,0)
OLd_chap = Properties("OldChap",500,0)
print(Players.Call_Money(vedant))
print(Players.Call_Props(vedant))
Players.Buy(vedant)
print(Players.Call_Props(vedant))
