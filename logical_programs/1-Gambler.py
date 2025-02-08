'''Simulates a gambler who start with $stake and place fair $1 bets until
he/she goes broke (i.e. has no money) or reach $goal. Keeps track of the number of
times he/she wins and the number of bets he/she makes. Run the experiment N
times, averages the results, and prints them out.'''

import random

stake=int(input("Enter the amount to put at stake : "))
goal=int(input("Enter the amount of the goal that you want to achieve : "))
times=int(input("Enter the number of times would you like to play : "))

wins=0
losses=0
for value in range(0,times):
    balance = stake

    while (0<balance<goal): # Will go until he gets broke and reachs his goal
        mutliplier=random.randrange(0,2)
        if mutliplier==0:
            balance-=1*1        
        elif mutliplier>0:
            balance+=1*mutliplier
    if balance==goal:
        wins+=1
    else:
        losses+=1


print(f'Times Won: {wins} \nWin : {(wins/times)*100:.2f}\nLosses : {(losses/times)*100:.2f}')
