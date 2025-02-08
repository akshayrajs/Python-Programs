#Sum of three Integer adds to ZERO

def triplet_zero(arr):
    distinct_value=[]
    n=len(arr)
    for first in range(n):
        for second in range(first,n):
            for third in range (second,n):
                if arr[first]+arr[second]+arr[third]==0:
                    distinct_value.append([first,second,third])
    return distinct_value

arr = [0,-1,-2,1,2]
print(triplet_zero(arr))