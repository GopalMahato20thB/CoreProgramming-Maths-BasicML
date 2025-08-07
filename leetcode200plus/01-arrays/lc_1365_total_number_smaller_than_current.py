"""
Given the array nums, for each nums[i],
find out how many numbers in the array are smaller than it.
Return the answer in an array.
"""

def smaller_than_current(nums):
    result = []
    for i in range(len(nums)):
        count = 0
        for j in range(1, len(nums)):
            if nums[j] < nums[i]:
                count += 1
        result.append(count)    
    return result

print(smaller_than_current([8, 1, 2, 2, 3]))                    
                
