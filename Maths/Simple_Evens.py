"""
Problem Statement                                            
  Have the function SimpleEvens(num) check whether every single
  number in the passed in parameter is even. If so, return the  
  string true, otherwise return the string false. For example: 
  if num is 4602225 your program should return the string      
  false because 5 is not an even number.                       
                                                               
  Examples                                                     
  Input 1: 2222220222 		                                
  Output 1: true                                               
                                                               
  Input 2: 20864646452                                         
  Output 2: false   
"""

"""
Algorithm:

1. Convert the given number `num` to a string.
2. Iterate through each character `ch` in the string.
3. For each character `ch`:
     - Check if the integer value of `ch` is odd.
     - If any character is odd, return "false".
4. If all characters are even, return "true".
"""


def SimpleEvens(num):
    num_str = str(num)
    for ch in num_str:
        if int(ch) % 2 != 0:
            return "false"
    return "true"

# Test Case 1
num = 2222220222
print(f"Input: {num}")
print(f"Output: {SimpleEvens(num)}")
print()

# Test Case 2
num = 20864646452
print(f"Input: {num}")
print(f"Output: {SimpleEvens(num)}")
print()

# Test Case 3
num = 0
print(f"Input: {num}")
print(f"Output: {SimpleEvens(num)}")
print()

# Test Case 4
num = 24686420
print(f"Input: {num}")
print(f"Output: {SimpleEvens(num)}")
print()

# Test Case 5
num = 135791113
print(f"Input: {num}")
print(f"Output: {SimpleEvens(num)}")
print()
