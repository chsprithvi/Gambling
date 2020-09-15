"""
A player with stake $100 and who bets $1 for each game.
Displaying the total Winning and Loosing days for each month.
Considering profit or loss for a month
"""
import random 
stake=100
bet=1
print("The player stake value:",stake)
print("The player bet value for the game :",bet)

percentLimit=0.5
minStake=stake-(stake*percentLimit)
maxStake=stake+(stake*percentLimit)

days=30
day=1
daysWon=0
daysLost=0
storeDaysWon={}
storeDaysLost={}

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
    storeDaysWon[day]=wonPerDay
    storeDaysLost[day]=lostPerDay

    day=day+1


print(storeDaysLost)
print(storeDaysWon)
luckyDay=max(storeDaysWon, key=storeDaysWon.get)
unLuckyDay=max(storeDaysLost, key=storeDaysLost.get)

print("The luckiest day in the month is",luckyDay,"with profit",storeDaysWon[luckyDay])
print("The Un-luckiest day in the month is",unLuckyDay,"with loss",storeDaysLost[unLuckyDay])


