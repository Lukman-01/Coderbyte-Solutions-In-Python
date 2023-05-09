"""
Problem Statement                                            
  Have the function OffBinary(strArr) read the array of strings 
  stored in strArr, which will contain two elements, the first 
  will be a positive decimal number and the second element will 
  be a binary number. Your goal is to determine how many digits 
  in the binary number need to be changed to represent the     
  decimal number correctly (either 0 change to 1 or vice versa)
                                                                
  For example: if strArr is ["56", "011000"] then your program 
  should return 1 because only 1 digit needs to change in the  
  binary number (the first zero needs to become a 1) to        
  correctly represent 56 in binary.                            
                                                               
  Examples                                                     
  Input 1: ["5624", "0010111111001"]                           
  Output 1: 2                                                  
                                                               
  Input 2: ["44", "111111"]                                    
  Output 2: 3           
"""

"""
    Algorithm
1. Convert the decimal number to binary.
2. Pad the binary number with leading zeros if necessary to make it the same length as the binary number in the input.
3. Loop over each digit in the binary number.
4. If the digit in the binary number does not match the corresponding digit in the binary representation 
    of the decimal number, increment a counter variable.
5. After looping over all the digits, return the counter variable as the result.
"""


def OffBinary(strArr):
    # Convert the decimal number to binary and remove the "0b" prefix
    dec = int(strArr[0])
    bin_str = bin(dec)[2:]
    
    # Pad the binary string with leading zeros if necessary
    if len(bin_str) < len(strArr[1]):
        bin_str = "0"*(len(strArr[1])-len(bin_str)) + bin_str
    
    # Loop over the binary strings and count the number of different bits
    count = 0
    for i in range(len(bin_str)):
        if bin_str[i] != strArr[1][i]:
            count += 1
            
    return count

# Test cases
print(OffBinary(["56", "011000"]))   # Output: 1
print(OffBinary(["5624", "0010111111001"]))   # Output: 2
print(OffBinary(["44", "111111"]))   # Output: 3
