"""
A player with stake $100 and who bets $1 for each game.
Displaying the total Winning and Loosing amount for 20 days.
"""
import random 
stake=100
bet=1
print("The player stake value:",stake)
print("The player bet value for the game :",bet)

percentLimit=0.5
minStake=stake-(stake*percentLimit)
maxStake=stake+(stake*percentLimit)

days=20
day=1
totalLost=0
totalWon=0
daysWon=0
daysLost=0

while day <= days:
    
    amount=stake
    wonPerDay=0
    lostPerDay=0
    
    while amount > minStake and amount < maxStake:
        """
        Winning=0
        Loosing=1
        """
        if random.randint(0,1) == 1:
            amount=amount-bet
            lostPerDay=lostPerDay+1
        else:
            amount=amount+bet
            wonPerDay=wonPerDay+1
    print("Won on",day,"is",wonPerDay,"lost on",day,"is",lostPerDay)
    totalLost=totalLost+lostPerDay
    totalWon=totalWon+wonPerDay
    day=day+1
print("Total won for",days,"is",totalWon,"Total lost for",days,"is",totalLost)

