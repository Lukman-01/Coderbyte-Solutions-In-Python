"""
Problem Statement                                            
  Have the function BinaryReversal(str) take the str parameter 
  being passed, which will be a positive integer, take its     
  binary representation (padded to the nearest N * 8 bits),    
  reverse that string of bits, and then finally return the new 
  reversed string in decimal form. For example: if str is "47" 
  then the binary version of this integer is 101111 but we pad 
  it to be 00101111. Your program should reverse this binary   
  string which then becomes: 11110100 and then finally return  
  the decimal version of this string, which is 244.            
                                                               
  Examples                                                     
  Input 1: "213"                                               
  Output 1: 171                                                
                                                               
  Input 2: "4567"                                              
  Output 2: 60296 

"""

# Algorithm
# 1. Convert the input string to an integer.
# 2. Convert the integer to its binary representation using the built-in `bin()` function.
# 3. Remove the '0b' prefix from the binary string.
# 4. Pad the binary string with leading zeros to make its length a multiple of 8 
# (i.e., nearest N * 8 bits), where N is the minimum number of bytes required to represent the binary string.
# 5. Reverse the padded binary string.
# 6. Convert the reversed binary string to its decimal representation using the built-in `int()` function with base 2.
# 7. Return the decimal representation as the output.


def BinaryReversal(strParam):
    # Convert input string to integer
    num = int(strParam)
    # Convert integer to binary string
    binary_str = bin(num)
    # Remove '0b' prefix from binary string
    binary_str = binary_str[2:]
    # Calculate minimum number of bytes required to represent the binary string
    num_bytes = (len(binary_str) + 7) // 8
    # Pad binary string with leading zeros to make its length a multiple of 8
    binary_str = binary_str.zfill(num_bytes * 8)
    # Reverse binary string
    reversed_binary_str = binary_str[::-1]
    # Convert reversed binary string to decimal representation
    decimal_num = int(reversed_binary_str, 2)
    return str(decimal_num)

# Test case 1
result1 = BinaryReversal("213")
print(result1)  # Output should be "171"

# Test case 2
result2 = BinaryReversal("4567")
print(result2)  # Output should be "60296"

# Test case 3
result3 = BinaryReversal("123")
print(result3)  # Output should be "222"
