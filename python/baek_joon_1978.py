# A faster and more effective way
# Method 1: Check up to the square root of itself (math library or **0.5)
# Method 2: Sieve of Eratosthenes
# -> The representative algorithms used to determine whether multiple numbers are prime or not.

import sys

num = int(sys.stdin.readline())
num_list = list(map(int, sys.stdin.readline().strip().split()))

count = 0
for element in num_list:
    # 1 is not a prime number
    if element == 1:
        continue

    prime = True
    for i in range(2, int(element**0.5)+1):
        if element % i == 0:
            prime = False
            break

    if prime:
        count += 1

print(count)
