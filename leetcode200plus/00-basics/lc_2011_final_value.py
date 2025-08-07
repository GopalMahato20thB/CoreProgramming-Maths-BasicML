"""
There is a variable x initially set to 0.

You are given a list of operations, where each operation is a string that can be one of the following:
"++X" → Increment x by 1
"X++" → Increment x by 1
"--X" → Decrement x by 1
"X--" → Decrement x by 1
Return the final value of x after performing all operations
"""
def final_value(operation):
    X = 0
    for op in operation:
        if "++" in op:
            X += 1
        else:
            X -= 1

    return X

print(final_value(["--X","X++","X++"]))                    
