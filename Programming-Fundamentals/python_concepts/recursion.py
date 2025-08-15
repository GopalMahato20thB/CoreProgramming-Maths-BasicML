"""
Recursion is a function calling itself.
Recursion is when solution of a problem depends on some smaller problem.
"""
def printNum(num):
    print(num)
    if num == 1:
        return "Completed"
    else:
        printNum(num - 1)
print(printNum(7))
            
