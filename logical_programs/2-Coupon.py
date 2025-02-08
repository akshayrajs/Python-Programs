'''Given N distinct Coupon Numbers, how many random numbers do you
need to generate distinct coupon number? This program simulates this random
process.'''

import random

class Coupon(): 
    def __init__(self,no_of_coupon,start,end): #auto initialize when called
        self.no_of_coupon=no_of_coupon
        self.start=start
        self.end=end

        arr=[]
        distinct=0
        
        while(distinct!=no_of_coupon): # Will run until we get N number of distinct coupon
            unique = random.randrange(start,end)
            if unique not in arr:
                arr.append(unique)
                distinct+=1
        print(arr)

no_of_coupon = int(input("Enter the number of coupon to generate : "))
start = int(input("Enter the start range of coupon : "))
end = int(input("Enter the end range of coupon : "))

Coupon(no_of_coupon,start,end) 