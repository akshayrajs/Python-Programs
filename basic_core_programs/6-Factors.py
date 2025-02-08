#Prime Factorial 

def prime(num): #function to check prime number
    if num<=1:
        return False
    for value in range(2,(num//2)+1):  
        if (num%value==0): #if divisible not a prime number
            return False
    return True

while True:
    try:
        number = int(input("Enter the nth value to find the prime factor : "))
        break
    except:
        print("Enter")
if number==1 or number==2:
    print(number)
else:
    fact=1
    for value in range(2,number+1):
        if prime(value)==True:
            print('yes')
            fact*=value #factorial

    print(fact)