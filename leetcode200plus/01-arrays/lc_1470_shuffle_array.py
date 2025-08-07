"""
Given the array nums consisting of 2n elements in the form:
[x1,x2,...,xn,y1,y2,...,yn],
return the array in the form:
[x1,y1,x2,y2,...,xn,yn].
"""
def suffle_array(nums, n):
    res = []
    for i in range(n):
        res.append(nums[i])
        res.append(nums[i + n])
    return res

print(suffle_array([2, 5, 1, 3, 4, 7], 3))
        
