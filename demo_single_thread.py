
import math
import time





start = time.time()

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n))+1):
        if n%i == 0:
            return False
        
    return True

def sum_prime(n):
    start_time = time.time()
    sum = 0
    for i in range(2,n):
        if is_prime(i):
            sum += i
    end_time = time.time()
    duration = end_time-start_time

    print(f"For range till {n} the Sum: {sum} in {duration:.4f} seconds")
    print("-"*40)
    



for i in range(1000,100000,1000):
    sum_prime(i)

end = time.time()
duration = end-start

print(f"Completed in {duration:.4f}")
