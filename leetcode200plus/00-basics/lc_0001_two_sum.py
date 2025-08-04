"""
Problem Statement
🧩 Problem Statement:
You are given an array of integers nums and an integer target.
Return True if there exist two distinct indices i and j such that
nums[i] + nums[j] == target
"""
## I Will use hashmap THE optimal solution for this problem 
def find_index(nums, target):
    track = {}
    for i, n in enumerate(nums):
        diff = target - n 
        if diff in track:
            return [track[diff], i]
        track[n] = i 
print(find_index([2, 7, 11, 15], 9))        
