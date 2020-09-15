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
    if wonPerDay > lostPerDay:
        daysWon=daysWon+1 
    else: 
        daysLost=daysLost+1
    
    totalLost=totalLost+lostPerDay
    totalWon=totalWon+wonPerDay
    day=day+1

diffAmount = totalWon - totalLost

print("Number of days won",daysWon, "Number of days lost",daysLost,"in 30 days")

if diffAmount>0:
    print("profit for overall month:",diffAmount )
elif diffAmount<0:
    print("loss for overall month:",abs(diffAmount))
else:
    print("Neither loss nor profit",diffAmount)