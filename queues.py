# Queue
# From queue module
# Simple Queue
# First In First Out
# Specialized for multi-threaded programming
# Few operations


# Deque
# From collections module
# Double Ended Queue
# FIFO, Last In First Out
# Multithreaded support
# More operations
# High performance and poping from both ends of the deque

from collections import deque
import random

@profile
def main():
    SIZE = 1_000_000
    big_list = list(range(SIZE))
    big_queue = deque(big_list)
    
    while big_list:
        big_list.pop() #pop all items from the END of the list
    while big_queue:
        big_queue.pop()  #pop all items from the END of the list

    big_list = list(range(SIZE))
    big_queue = deque(big_list)
    
    while big_list:
        big_list.pop(0)  #pop all items from the START of the list (This is a very slow operation)
    while big_queue:
        big_queue.popleft()  #pop all items from the START of the deque

main()