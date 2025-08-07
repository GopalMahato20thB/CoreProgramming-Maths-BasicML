"""
Given an array nums, return the running sum of nums.

The running sum at index i is the sum of all elements from nums[0] to nums[i] (inclusive).

Example: 
Input: nums = [1, 2, 3, 4]
Output: [1, 3, 6, 10]

# Explanation:
# runningSum[0] = 1
# runningSum[1] = 1 + 2 = 3
# runningSum[2] = 1 + 2 + 3 = 6
# runningSum[3] = 1 + 2 + 3 + 4 = 10

"""

def running_sum(nums):
    for i in range(1, len(nums)):
        nums[i] += nums[i - 1]
    return nums        
    
        
print(running_sum([1, 2, 3, 4]))    
        
        


