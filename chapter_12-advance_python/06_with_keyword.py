'''
we can use multiple cotext manager in a single with statement.

Syntax:
    with context_manager1 as var1, context_manager2 as var2:
        # code block
        pass
        
Example:
    with open("file1.txt") as file1, open("file2.txt") as file2:
        # code block
        pass

'''

# Example 1: Multiple Context Managers
with open("file1.txt") as file1, open("file2.txt") as file2:
    # code block
    pass


