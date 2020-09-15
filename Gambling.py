"""
A player with stake $100 and who bets $1 for each game
Wins $1 if won and looses $1 is lost
"""
import random 
stake=100
bet=1
print("The player stake value:",stake)
print("The player bet value for the game :",bet)

"""
Winning=0
Loosing=1
"""
if random.randint(0,1) == 1:
    print("~~~~~~You Lost~~~~~~")
    print("The stake value after Loosing:",stake-bet)
else:
    print("~~~~~~You Won~~~~~~")
    print("The stake value after Winning:",stake+bet)
