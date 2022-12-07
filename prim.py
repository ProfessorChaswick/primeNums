import math
import time

def is_prime_v1(n): # First version of the function
    """Return 'true' if n is a prime number and 'false' if it is composit."""
    if n == 1: 
        return False

    for xx in range(2,n):
        if n % xx == 0:
            return False
        
    return True

def is_prime_v2(n): # First version of the function
    """Return 'true' if n is a prime number and 'false' if it is composit."""
    if n == 1: 
        return False
    max_divisor = math.floor(math.sqrt(n))
    for xx in range(1, 1 + max_divisor):
        if n % xx == 0:
            return False
    return True


# Test function
# for n in range(1,21):
#     print(n, is_prime_v1(n))

# Time the function
tStart = time.time()
for n in range(1, 100001):
    is_prime_v1(n)

tStop = time.time()

print(tStop - tStart)

tStart = time.time()
for n in range(2, 100001, 2):
    is_prime_v2(n)

tStop = time.time()

print(tStop - tStart)