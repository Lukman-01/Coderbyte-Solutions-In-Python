"""
Problem Statement                                            
  Have the function HappyNumbers(num) determine if a number is	
  Happy, which is a number whose sum of the square of the	
  digits eventually converges to 1. Return true if it's a Happy
  number, otherwise return false.       			
                                                               
  For example: the number 10 is Happy because 1^2 + 0^2	
  converges to 1.       					
                                                               
  Examples                                                     
  Input 1: 1		                                        
  Output 1: true                                               
                                                               
  Input 2: 101		                                        
  Output 2: false      
"""

"""
Algorithm:

1. Create a helper function `get_next_number` that takes an integer `num` 
    as input and returns the sum of the squares of its digits.
2. Initialize a variable `current_number` to the given number `num`.
3. Create an empty set `visited` to keep track of the numbers encountered.
4. Iterate until `current_number` becomes 1 or `current_number` is already present in the `visited` set:
     - Add the `current_number` to the `visited` set.
     - Update `current_number` by calling the `get_next_number` function with `current_number` as the argument.
5. If `current_number` becomes 1, return `True`; otherwise, return `False`.
"""


def get_next_number(num):
    digit_squares = [int(digit) ** 2 for digit in str(num)]
    return sum(digit_squares)

def HappyNumbers(num):
    current_number = num
    visited = set()

    while current_number != 1 and current_number not in visited:
        visited.add(current_number)
        current_number = get_next_number(current_number)

    return current_number == 1


# Test Case 1
num = 1
print(f"Input: {num}")
print(f"Output: {HappyNumbers(num)}")
print()

# Test Case 2
num = 101
print(f"Input: {num}")
print(f"Output: {HappyNumbers(num)}")
print()

# Test Case 3
num = 7
print(f"Input: {num}")
print(f"Output: {HappyNumbers(num)}")
print()

# Test Case 4
num = 19
print(f"Input: {num}")
print(f"Output: {HappyNumbers(num)}")
print()

# Test Case 5
num = 22
print(f"Input: {num}")
print(f"Output: {HappyNumbers(num)}")
print()
