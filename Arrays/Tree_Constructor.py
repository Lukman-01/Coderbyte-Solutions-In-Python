"""
Tree Constructor
Have the function TreeConstructor(strArr) take the array 
of strings stored in strArr, which will contain pairs 
of integers in the following format: (i1,i2), 
where i1 represents a child node in a tree and the 
second integer i2 signifies that it is the parent of i1. 
For example: if strArr is ["(1,2)", "(2,4)", "(7,2)"], 
then this forms the following tree:



which you can see forms a proper binary tree. Your program should, 
in this case, return the string true because a valid binary tree 
can be formed. If a proper binary tree cannot be formed with the 
integer pairs, then return the string false. All of the integers 
within the tree will be unique, which means there can only be one 
node in the tree with the given integer value.
Examples
Input: ["(1,2)", "(2,4)", "(5,7)", "(7,2)", "(9,5)"]
Output: true
Input: ["(1,2)", "(3,2)", "(2,12)", "(5,2)"]
Output: false
"""

# Algorithm:
# 1. Create a dictionary to store the parent node and its children.
# 2. For each pair (i1, i2) in strArr, check if i2 is already a parent node or not. If it's not, then create a new key-value pair in the dictionary with i2 as the key and i1 as the value.
# 3. If i2 is already a parent node, then check if it already has 2 children. If it doesn't have 2 children, add i1 as a child. If it already has 2 children, return false because it's not a proper binary tree.
# 4. After iterating through all pairs, check if there is only one root node. If there is, return true. If there isn't, return false because it's not a proper binary tree.


def TreeConstructor(strArr):
    parent_children = {}
    for pair in strArr:
        i1, i2 = pair.strip('()').split(',')
        if i2 not in parent_children:
            parent_children[i2] = [i1]
        elif len(parent_children[i2]) == 2:
            return "false"
        else:
            parent_children[i2].append(i1)
    root_count = 0
    for parent in parent_children:
        if parent not in [child for children in parent_children.values() for child in children]:
            root_count += 1
    return "true" if root_count == 1 else "false"
 

#Test Case 1
print(TreeConstructor(["(1,2)", "(2,4)", "(5,7)", "(7,2)", "(9,5)"])) #"true"

#Test Case 2
print(TreeConstructor(["(1,2)", "(3,2)", "(2,12)", "(5,2)"])) #"false"

#Test Case 3
print(TreeConstructor(["(1,2)", "(2,4)", "(4,8)", "(8,16)", "(16,32)", "(32,64)"])) #"true"

#Test Case 4
print(TreeConstructor(["(1,2)", "(2,3)", "(3,4)", "(4,5)", "(5,6)", "(6,7)", "(7,8)"]))  #"true"

#Test Case 5
print(TreeConstructor(["(1,2)", "(2,3)", "(2,4)", "(4,5)", "(4,6)", "(6,7)", "(6,8)"])) #"false"
