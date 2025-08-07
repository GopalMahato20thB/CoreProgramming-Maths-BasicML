"""
You are given an integer array candies,
where each element represents the number of
candies a kid has. You are also given an integer
extraCandies, which represents the number of extra
candies you can give to each kid.

Return a list of booleans. For each kid,
check if after giving them the extra candies,
they will have the greatest number of candies among all the kids.


Input: 
candies = [2, 3, 5, 1, 3]
extraCandies = 3

Output:
[True, True, True, False, True]

Explanation:
Kid 0: 2 + 3 = 5 → max = 5 → ✅
Kid 1: 3 + 3 = 6 → > 5 → ✅
Kid 2: 5 + 3 = 8 → > 5 → ✅
Kid 3: 1 + 3 = 4 → < 5 → ❌
Kid 4: 3 + 3 = 6 → > 5 → ✅
"""
def kids_with_candies(candies, extraCandies):
    max_candies = max(candies)
    result = []

    for candy in candies:
        if candy + extraCandies >= max_candies:
            result.append(True)
        else:
            result.append(False)
    return result

print(kids_with_candies([2, 3, 5, 1, 3], 3))
                
