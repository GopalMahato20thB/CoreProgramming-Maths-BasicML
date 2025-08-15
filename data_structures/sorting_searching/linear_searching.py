"""
Linear Search:
time O (n^2) space O(1)
"""

def linear_search(arr, target):

    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return - 1
             


nums = [1, 4, 7, 3, 99]        
target = 7

print(linear_search(nums, target))
