'''Tic Tac Toe'''
import os, random

def empty_grid(arr): # creating a empty grid
    count=1
    for row in range(3):
        temp=[]
        
        for column in range(3):
            empty=count
            count+=1
            temp.append(empty)
        
        arr.append(temp) 
        
def grid_printer(arr): # a cool cli tic tac toe printer
    os.system('cls')
    for row in range(3):
        for column in range(3):
            print(f' {arr[row][column]}',end='') 
            
            if column<2:
                print(" |",end='') # aesthetic

        if row<2:
            print("\n-----------") # seprator

        else:
            print("\n")

def checker(arr):
    for index in range(3):
        if arr[index][0]==arr[index][1]==arr[index][2]: # finds if there are any same symbol in vertically
            grid_printer(arr)
            print(f'{arr[index][0]} Won The Game!!!!')
            exit()

        elif arr[0][index]==arr[1][index]==arr[2][index]: # finds if there are any same symbol in horizontally
            grid_printer(arr)
            print(f'{arr[index][0]} Won The Game!!!!')
            exit()

        elif arr[0][0]==arr[1][1]==arr[2][2]: # finds if there are any same symbol in diagonally from left corner
            grid_printer(arr)
            print(f'{arr[0][0]} Won The Game!!!!')
            exit()

        elif arr[0][2]==arr[1][1]==arr[2][0]: # finds if there are any same symbol in diagonally from right corner
            grid_printer(arr)
            print(f'{arr[0][2]} Won The Game!!!!')
            exit()

        else:
            continue

def filler(arr,turn): # provide what cells are empty
    number = [1,2,3,4,5,6,7,8,9]
    
    while True:
        try:
            if turn=='X':
                cell=int(input("Enter the cell you would like to fill in number : "))
            else:
                cell=random.choice(number)
            count=1
            for row in range(3):
                for column in range(3):
                    if cell==arr[row][column]:
                        number.pop(cell-1)
                        arr[row][column]=turn
                        return arr
                    count+1
            print("Wrong Input or Already Filled")
        except:
            print("Invalid Input")

def initiator():
    arr=[]
    empty_grid(arr)
    
    for x in range(9):
        grid_printer(arr)      
        
        if x%2==0:
            turn='X'
            print(f"Its {turn}'s Turn")
        else:
            turn='O'
            print(f"Its {turn}'s Turn")
        
        filler(arr,turn)
        checker(arr)
    print("Draw")    


if __name__ == "__main__":
    initiator()
