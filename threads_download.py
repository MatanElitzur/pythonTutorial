import threading
from urllib import request

# This code example how multi threding is better in perormence then single threding.

def download():
    return request.urlopen('https://google.com').read()

def single_thred():
    for _ in range(5):
        download()
    
def multiple_thread():
    threads = []
    for _ in range(5):
        threads.append(threading.Thread(target=download)) 
    for t in threads:
        t.start() # Start all the threads
    for t in threads:
        t.join() # Wait for all the threads to finish their work

@profile
def main():
    single_thred()
    multiple_thread()
# Execute --> kernprof -l -v threads_2.py    
