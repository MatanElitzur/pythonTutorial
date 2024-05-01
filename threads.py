import threading
from time import sleep
# this code display how to use threads in python

#First approach
class orderProcessing(threading.Thread): # Create a subclass of Thread
    def run(self):
        print(f"Processing order")

#Second approach
def process_order(order_id):
    print(f"Processing with id: {order_id}")
    sleep(1)
    print(f"Done processing id: {order_id}")

def main():
    #Second approach
    t = threading.Thread(target=process_order, args=(10,)) # Create a thread with a target function
    t.start() # Start the thread

    #First approach
    thread = orderProcessing() # Create an instance of the subclass
    thread.start() # Start the thread

#Execute --> python3 threads.py
main()
# How to synchronize threads
# 1.) Locks
# 2.) Semaphores
# 3.) Condition variables


# Async
# 1.) Low overhead
# 2.) Low potential for bugs
# 3.) Learning curve
# 4.) Compatibility constraint

# Threads
# 1.) High overhead
# 2.) High potential for bugs
# 3.) Simple syntax
# 4.) High compatibility