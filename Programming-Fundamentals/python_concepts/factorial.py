"""
import sys
print(sys.getrecursionlimit())

sys.setrecursionlimit(100)
print(sys.getrecursionlimit())
"""

def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)

print(factorial(7))    

"""
We have to make sure that recursion stops somewhere and don't keep on going.
We add a base case.

"""
