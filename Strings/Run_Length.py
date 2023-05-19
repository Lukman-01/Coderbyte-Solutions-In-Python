"""
Problem Statement                                            
  Have the function RunLength(str) take the str parameter being
  passed and return a compressed version of the string using   
  the Run-length encoding algorithm. This algorithm works by   
  taking the occurrence of each repeating character and        
  outputting that number along with a single character of the  
  repeating sequence.                                          
  For example: "wwwggopp" would return 3w2g1o2p.               
  The string will not contain any numbers, punctuation,        
  or symbols.                                                  
                                                               
  Examples                                                     
  Input 1: "aabbcde"                                           
  Output 1: 2a2b1c1d1e                                         
                                                               
  Input 2: "wwwbbbw"                                           
  Output 2: 3w3b1w          
"""

"""
Algorithm
1. Initialize an empty string `compressed_str` to store the compressed version of the input string.
2. Initialize a variable `count` to 1 to keep track of the consecutive occurrences of a character.
3. Iterate over each character `c` in the input string starting from the second character.
   - If the current character `c` is equal to the previous character, increment the `count` variable.
   - If the current character `c` is different from the previous character, append the `count` followed by the previous character to `compressed_str`, reset the `count` to 1, and update the previous character.
4. After the loop, append the final `count` followed by the last character to `compressed_str`.
5. Return the `compressed_str`.
"""


def RunLength(strParam):
    if not strParam:
        return ""  # Return empty string if input is empty

    compressed_str = ""
    count = 1
    previous_char = strParam[0]

    for i in range(1, len(strParam)):
        current_char = strParam[i]

        if current_char == previous_char:
            count += 1
        else:
            compressed_str += str(count) + previous_char
            count = 1
            previous_char = current_char

    compressed_str += str(count) + previous_char
    return compressed_str


print(RunLength("aabbcde"))
# Output: 2a2b1c1d1e

print(RunLength("wwwbbbw"))
# Output: 3w3b1w

print(RunLength("a"))
# Output: 1a

print(RunLength(""))
# Output: ""

print(RunLength("ccc"))
# Output: 3c
