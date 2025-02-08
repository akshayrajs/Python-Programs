'''a program Distance.java that takes two integer command-line arguments x
and y and prints the Euclidean distance from the point (x, y) to the origin (0, 0). The
formulae to calculate distance = sqrt(x*x + y*y). Use Math.power function'''

import sys
x=int(sys.argv[1]) #command line argument 1 as x
y=int(sys.argv[2]) #command line argument 2 as y

print(f"Distance : {(x*x+y*y)**0.5:.3f}")

