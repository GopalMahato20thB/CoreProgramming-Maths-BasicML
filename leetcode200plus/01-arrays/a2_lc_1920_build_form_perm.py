"""
You are given a zero-based permutation array nums of length n.
You have to build an array ans such that:
ans[i] = nums[nums[i]]

"""

def build_array(nums):
    res = []
    for i  in range(len(nums)):
        res.append(nums[nums[i]])
    return res

print(build_array([0, 2, 1, 5, 3, 4]))



