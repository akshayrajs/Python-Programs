'''Simulate Stopwatch Program'''

import time

start = input("Press Enter to start the stopwatch.... ")
start_time=time.time()
print("Running......")
stop = input("Press Enter to stop the stopwatch.... ")
stop_time=time.time()

print(f'Time elapsed {stop_time-start_time:.2f}')