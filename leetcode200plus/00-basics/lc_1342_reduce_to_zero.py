"""
Given an integer num, return the number of steps to reduce it to zero.

In one step:
If num is even, divide it by 2.
If num is odd, subtract 1.

>>> Example 1
Input: num = 14
Output: 6

# Explanation:
# Step 1: 14 is even → 14 / 2 = 7
# Step 2: 7 is odd → 7 - 1 = 6
# Step 3: 6 is even → 6 / 2 = 3
# Step 4: 3 is odd → 3 - 1 = 2
# Step 5: 2 is even → 2 / 2 = 1
# Step 6: 1 is odd → 1 - 1 = 0
"""
def reduce_to_zero(num):
    count = 0
    
    while num != 0:
        count += 1
        if num % 2 == 0:
            num = num // 2
        elif num % 2 != 0:
            num = num - 1
    return count

print(reduce_to_zero(14))
print(reduce_to_zero(8))
print(reduce_to_zero(123))


