from multiprocessing import Process, Lock
import math
import time


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n))+1):
        if n%i == 0:
            return False
        
    return True

def sum_prime(n,print_lock):
    start_time = time.time()
    sum = 0
    for i in range(2,n):
        if is_prime(i):
            sum += i
    end_time = time.time()
    duration = end_time-start_time

    with print_lock:
        print(f"For range till {n} the Sum: {sum} in {duration:.4f} seconds")
        print("-"*40)
    

if __name__ == "__main__":
    print_lock = Lock()
    start = time.time()

    processes = []

    for i in range(100000,1100000,100000):
        p = Process(target=sum_prime,args=(i,print_lock))
        processes.append(p)
        p.start()

    for i in processes:
        i.join()

    end = time.time()
    duration = end-start

    print(f"All processes completed in {duration:.4f}")
