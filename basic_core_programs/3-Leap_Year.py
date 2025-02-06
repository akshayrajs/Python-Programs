#Leap Year

while True:
    try:
        year=int(input("Enter the year:"))
        if len(str(year))>=4: #checks if the input is positive or not
            break
        else:
            print("Error : The year should consist four digits")
    except:
        print("Wrong Input")

if (year%4==0 and year%100==0) or year%400==0: #checks for leap year
    print("Leap year!")
else:
    print("Not a leap year!")