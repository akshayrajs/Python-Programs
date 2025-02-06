#Find power of two

import sys

n=int(sys.argv[1]) #taking value from command line

while True:
    try:
        if n>0 and n<31:
            value=pow(n,2)
            break
        else:
            print("Try Again! This Value overflows int.")
            quit()
    except:
        print("Wrong Input")

if (n%4==0 and n%100==0) or n%400==0: #checking leap year
    print("Leap year!")
else:
    print("Not a leap year!")
