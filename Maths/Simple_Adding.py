"""
Have the function SimpleAdding(num) add up all the numbers from 1 to num. 
For example: if the input is 4 then your program should return 10 
because 1 + 2 + 3 + 4 = 10. For the test cases, the parameter 
num will be any number from 1 to 1000.

Examples
Input: 12
Output: 78

Input: 140
Output: 9870
"""


# Algorithm:
# 1. Define a function called `SimpleAdding` that takes one parameter `num`.
# 2. Initialize a variable `sum` to 0.
# 3. Use a loop to iterate from 1 to `num` (inclusive).
# 4. In each iteration, add the current number to the `sum`.
# 5. After the loop completes, return the value of `sum`.



def SimpleAdding(num):
    sum = 0
    for i in range(1, num+1):
        sum += i
    return sum
 
    

print(SimpleAdding(4))   # Output: 10
print(SimpleAdding(12))  # Output: 78
print(SimpleAdding(140)) # Output: 9870
print(SimpleAdding(1))   # Output: 1
print(SimpleAdding(1000)) # Output: 500500
