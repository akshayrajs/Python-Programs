#Flip Coin and print percentage of Heads and Tails

import random

while True:
    try:
        flip_times=int(input("Enter the number of times to flip the coin : "))
        if flip_times>=0: #checks if the input is positive or not
            correct='yes'
            break
        else:
            print("Error : The number should be positive")
    except:
        print("Error: Wrong number value")

tails=0 #inital value for tails
heads=0 #inital value for heads
for x in range (0,flip_times):
    random_number=random.random() #Gets random number between 0.0 to 0.1
    if random_number < 0.5:
        tails+=1 # Counts the number of times tails occurs
    else:
        heads+=1 # Counts the number of times heads occurs

print(f"The Percentage Head is {(heads/flip_times)*100:.2f}%, Tails : {(tails/flip_times)*100:.2f}%")