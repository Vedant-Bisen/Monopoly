'''def start():
    c = "y"
    while (c == "y"):
        n = len(players)
        for i in range(0,n):
            players[i]["player_pos"] = players[i]["player_pos"]+dice_roll()
            pos = players[i]["player_pos"]
            print("You have landed on ",places[pos],"\n")
            ask = input("Do you wish to buy: ")
            if (ask == "yes"):
              upd = {"Owner":str(players[i])}
              places[pos].update(upd)
            elif (ask == "no"):
              break
            else:
              print("Please enter the right ans")
initial()'''

class home:
        name = "uppals"
        place = "hello"

print(home.name)