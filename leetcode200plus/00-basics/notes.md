# 🧠 Time & Space Complexity Notes

# 🔹 1. What is Time Complexity?
## Time complexity is a way to express how the runtime of an algorithm grows as the input size increases.

## 🔸 You Should Understand:
- Big-O Notation: O(1), O(n), O(log n), O(n log n), O(n^2), etc.

- Best, Worst, Average Case

- Examples of:
- Linear: Loop over array → O(n)
- Quadratic: Nested loop → O(n^2)
- Logarithmic: Binary search → O(log n)
- Constant time operations: O(1) → e.g., accessing an index in array.


# 2. What is Space Complexity?
Space complexity is the amount of memory or space your algorithm needs relative to the input size.

##🔸 You Should Understand:
- When does space increase? (e.g., creating new data structures)

- Examples:
- In-place operations → O(1)
- Creating array copies → O(n)

# 🔹 3. Time & Space Trade-offs
- Faster algorithms may use more memory, or vice versa. Understand which matters more for your use case.

# Analyzing Time & Space in Code

"""
def sum_array(arr):
    total = 0             # O(1)
    for num in arr:       # O(n)
        total += num
    return total          # O(1)
"""
- Time = O(n)
- Space = O(1)



## ✅ Time Complexity
- Constant: O(1)
- Linear: O(n)
- Quadratic: O(n^2)
- Logarithmic: O(log n)
- Linear Log: O(n log n)
- Exponential: O(2^n)

