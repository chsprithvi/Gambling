"""
A player with stake $100 and who bets $1 for each game, resigns if won/lost 50% of stake

"""
import random 
stake=100
bet=1
print("The player stake value:",stake)
print("The player bet value for the game :",bet)
percentLimit=0.5
minStake=stake-(stake*percentLimit)
maxStake=stake+(stake*percentLimit)

while stake > minStake and stake < maxStake:
    """
    Winning=0
    Loosing=1
    """
    if random.randint(0,1) == 1:
        print("~~~~~~You Lost~~~~~~")
        print("The stake value after Loosing:",stake-bet)
        stake=stake-bet
    else:
        print("~~~~~~You Won~~~~~~")
        print("The stake value after Winning:",stake+bet)
        stake=stake+bet
print("Sorry, Your stake value is limited to",stake)