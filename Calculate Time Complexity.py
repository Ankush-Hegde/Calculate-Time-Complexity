import time
initial_time = time.time()
m = input("Input a function: ")

ending_time = time.time()
total_time = ending_time - initial_time
print("\nThe time complexity of this function is: ",total_time)