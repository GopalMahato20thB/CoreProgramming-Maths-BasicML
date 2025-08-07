"""
You are given an integer array nums where the largest number is at least twice as much as every other number in the array.

Return the index of the largest number, or return -1 if no such number exists.
"""
# Function to find the index of the largest number
# that is at least twice as much as every other number

def dominantIndex(nums):
    # edge case: If the list has only two elements, I need to compare them
    if len(nums) == 2:
        if nums[0] >= 2 * nums[1]:
            return 0
        elif nums[1] >= 2 * nums[0]:
            return 1
        else:
            return -1

    # Now i need to initialize variables to keep track of the largest and the second largest
    max_value = -1
    second_max = -1
    max_index = -1
    
    # looping through array to find max and second max 
    for i, num in enumerate(nums):  
        if num > max_value:
            second_max = max_value
            max_value = num
            max_index = i
        elif num > second_max:
            second_max = num
    
    if max_value >= 2 * second_max:
        return max_index
    else:
        return -1

print(dominantIndex([3, 6, 1, 0]))    # Output: 1
print(dominantIndex([1, 2, 3, 4]))    # Output: -1        
    
#### writing this code one more time
def dominant_index(nums):
    if not nums:
        return -1
    max_value = float("-inf")
    second_max = float("-inf")
    max_index = -1
    
    for i, num in enumerate(nums):
        if num > max_value:
            second_max = max_value
            max_value = num
            max_index = i
        elif num > second_max:
            second_max = num
    
    if num >= 2 * second_max:
        return max_index
    return -1
        
            
print(dominant_index([1, 0, 0, 7])) #must return 3

