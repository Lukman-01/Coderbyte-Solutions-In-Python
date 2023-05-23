"""
Problem Statement                                            
  Have the function BinaryConverter(str) return the decimal    
  form of the binary value. For example: if 101 is passed      
  return 5, or if 1000 is passed return 8.                     
                                                               
  For example: the number 10 is Happy because 1^2 + 0^2	
  converges to 1.       					
                                                            
  Examples                                                    
  Input 1: "100101" 		                                
  Output 1: 37                                                 
                                                               
  Input 2: "011"                                               
  Output 2: 3                 
"""

"""
Algorithm:

1. Convert the binary string to an integer.
2. Initialize a variable `decimal` to 0.
3. Iterate through each character `ch` in the binary string from left to right.
4. For each character `ch`:
     - Multiply the current `decimal` value by 2.
     - Add the integer value of `ch` (0 or 1) to `decimal`.
5. Return the final `decimal` value.
"""


def BinaryConverter(str):
    decimal = 0
    for ch in str:
        decimal = decimal * 2 + int(ch)
    return decimal


# Test Case 1
input_str = "100101"
print(f"Input: {input_str}")
print(f"Output: {BinaryConverter(input_str)}")
print()

# Test Case 2
input_str = "011"
print(f"Input: {input_str}")
print(f"Output: {BinaryConverter(input_str)}")
print()

# Test Case 3
input_str = "0"
print(f"Input: {input_str}")
print(f"Output: {BinaryConverter(input_str)}")
print()

# Test Case 4
input_str = "111"
print(f"Input: {input_str}")
print(f"Output: {BinaryConverter(input_str)}")
print()

# Test Case 5
input_str = "101010"
print(f"Input: {input_str}")
print(f"Output: {BinaryConverter(input_str)}")
print()
