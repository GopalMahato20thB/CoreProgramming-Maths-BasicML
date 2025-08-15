import sys

sys.setrecursionlimit(1001)


def sum_of_num(num):
    if num == 1:
        return 1
    return num + sum_of_num(num - 1)
print(sum_of_num(5))
print(sum_of_num(10))        
print(sum_of_num(1000))        
