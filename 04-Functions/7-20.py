###
# Define the function f(n) that returns the n-th prime number. 
# A prime number is a natural number greater than 1, divisible by 1 and that number
#
import math

def prime(number):
    if number <= 1:
        return False
    for i in range(2, math.isqrt(number) + 1):
        if number % i == 0:
            return False
    return True

def f(n):
    count = 0
    num = 1
    while count < n:
        num += 1
        if prime(num):
            count += 1
    return num

print(f(1))
print(f(5))