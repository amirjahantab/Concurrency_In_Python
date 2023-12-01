import time
import threading, queue
import requests
from utils import is_prime, DEFAULT_NUMBERS
q = queue.Queue()


def get_page(number):

    while True:
        url = q.get()
        try:
            response = requests.get(url)
        except:
            print(f"Error occurred {url}")
        print(
            f"Worker {number}\t get completed {url}\t queue size {q.qsize()}"
            )
        q.task_done()
        if q.empty():
            break
        
        
def show_is_prime(worker_id):
    while True:
        number = q.get()
        is_prime(number)
        q.task_done()
        if q.empty():
            break
        

def multi_thread():
        
    for num in DEFAULT_NUMBERS:
        q.put(num)
        
    threads = []
    for i in range(6):
        t = threading.Thread(target=show_is_prime, args=(i, ))
        threads.append(t)
        t.setDaemon(True)
        t.start()
        
    q.join()
    print("threads joined")