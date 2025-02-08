#Harmonic Number

while True:
    try:
        n=int(input("Enter the nth value for the Harmonic Number : "))

        if n>0:
            break
        else:
            print("The value of n should be greater than 0")
    except:
        print("Wrong Input")

total=0
for value in range (1,n+1):
    total+=1/value # calculating harmonic number

print(f"{total:.2f}")