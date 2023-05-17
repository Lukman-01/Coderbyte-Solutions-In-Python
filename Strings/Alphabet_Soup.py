"""
Problem Statement                                            
  Have the function AlphabetSoup(str) take the str string      
  parameter being passed and return the string with the        
  letters in alphabetical order (ie. hello becomes ehllo).     
  Assume numbers and punctuation symbols will not be included  
  in the string.                                               
                                                               
  Examples                                                     
  Input 1: coderbyte                                           
  Output 1: bcdeeorty                                          
                                                               
  Input 2: hooplah                                             
  Output 2: ahhloop           
"""

# Algorithm:

# 1. Convert the input string to a list of characters.
# 2. Sort the list in alphabetical order.
# 3. Join the characters back together into a string.
# 4. Return the sorted string.


def AlphabetSoup(strParam):
  # Convert the input string to a list of characters
  chars = list(strParam)
  # Sort the list in alphabetical order
  chars.sort()
  # Join the characters back together into a string
  sorted_str = ''.join(chars)
  # Return the sorted string
  return sorted_str


result1 = AlphabetSoup("coderbyte")
print(result1)  # Output should be "bcdeeorty"

result2 = AlphabetSoup("hooplah")
print(result2)  # Output should be "ahhloop"

result3 = AlphabetSoup("HelloWorld")
print(result3)  # Output should be "HWdellloor"

result4 = AlphabetSoup("string!@$")
print(result4)  # Output should be "!$@ginrst"
