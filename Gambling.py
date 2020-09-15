"""
A player with stake $100 and who bets $1 for each game.
Displaying the total Winning and Loosing days for each month.
Considering profit or loss for a month
"""

import random 

"""
calculateMonth function helps in calculating daily profit and loss, returns difference b/w total lost and profit
"""

def calculateMonth():
    stake=100
    bet=1
    days=30
    day=1
    totalLost=0
    totalWon=0
    daysWon=0
    daysLost=0

    print("The player stake value:",stake)
    print("The player bet value for the game :",bet)
    
    percentLimit=0.5
    minStake=stake-(stake*percentLimit)
    maxStake=stake+(stake*percentLimit)


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
    print("Number of days won",daysWon, " and Number of days lost",daysLost,"in 30 days")
    diffAmount = totalWon - totalLost
    return(diffAmount)

"""
checkMonth fuction recurcively helps to check if profit or loss per month
"""

def checkMonth():
    checkProfitLoss=calculateMonth()

    if checkProfitLoss>0:
        print("profit for overall month:",checkProfitLoss)
        print("congrats! You can play for next month")
        
        flag=str(input("Press 'Y' to Continue or any other key to exit"))
    
        if flag=='y'or'Y':
            checkMonth()
        else:
            exit()
    elif checkProfitLoss<0:
        print("loss for overall month:",abs(checkProfitLoss))
        print("Sorry, You cannot continue next month. Better luck Next time :-) ")
    else:
        print("neither loss nor profit")
        print("Sorry, You cannot continue next month. Better luck Next time :-) ")

"""
****************
Main method calls the demo fuction to check if month has profit or loss
****************
"""

def main():
    print("Welcome to the World of Gambling")
    checkMonth()
if __name__ == "__main__":
    main()