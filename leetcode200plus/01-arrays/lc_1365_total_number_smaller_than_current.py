"""
Given the array nums, for each nums[i],
find out how many numbers in the array are smaller than it.
Return the answer in an array.
"""

def smaller_than_current(nums):    
    sorted_nums = sorted(nums)
    num_to_count = {}

    for idx, num in enumerate(sorted_nums):
        if num not in num_to_count:
            num_to_count[num] = idx

    return [num_to_count[num] for num in nums]        


print(smaller_than_current([8, 1, 2, 2, 3]))                    
                
