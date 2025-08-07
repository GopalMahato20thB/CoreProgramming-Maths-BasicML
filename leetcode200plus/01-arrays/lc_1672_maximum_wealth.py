"""
You are given an m x n integer grid accounts where
accounts[i][j] is the amount of money the i-th customer
has in the j-th bank.

Return the wealth that the richest customer has.
A customer's wealth is the sum of money they have in 
all their bank accounts. The richest customer is the
customer that has the maximum wealth.
Input: accounts = [[1,2,3],[3,2,1]]
Output: 6

# Explanation:
# - Customer 0 has wealth = 1 + 2 + 3 = 6
# - Customer 1 has wealth = 3 + 2 + 1 = 6
# So the richest customer has a wealth of max(6, 6) = 6

"""
def max_wealth(accounts):
    return max([sum(customer) for customer in accounts])
    
accounts = [[1, 2, 3], [3, 2, 1]]
print(max_wealth(accounts))    
