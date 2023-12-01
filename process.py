from multiprocessing import Pool
import time
from thread import multi_thread
from utils import is_prime, DEFAULT_NUMBERS


def multi_process():
    
    pool = Pool(4)
    
    with pool:
        pool.map(is_prime, DEFAULT_NUMBERS)
        
    print("All processes finished")