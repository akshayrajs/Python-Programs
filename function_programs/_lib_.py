'''A library for reading in 2D arrays of integers, doubles, or booleans from
standard input and printing them out to standard output.'''

def create_matrix(row, column, data_type=int): 
    matrix = []
    for x in range(row):
        temp = []
        for y in range(column):
            while True: 
                try:
                    if data_type == bool: # Boolean array
                        val = input(f"Enter the value for matrix [{x},{y}] (True/False/1/0): ").lower()
                        if val in ("true", "1"):
                            number = True
                        elif val in ("false", "0"):
                            number = False
                        else:
                            print("Invalid boolean value")
                    else: 
                        number = data_type(input(f"Enter the value for matrix [{x},{y}]: ")) # Data type is dynamic can be float or int
                    temp.append(number) #creating 1D array of input
                    break 
                except:
                    print("Invalid Data Type")
        matrix.append(temp) # appending to make it 2D array
    return matrix