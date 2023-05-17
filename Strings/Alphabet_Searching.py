"""
Problem Statement                                            
  Have the function AlphabetSearching(str) take the string     
  parameter being passed and return the string true if every   
  single letter of the English alphabet exists in the string,  
  otherwise return the string false.                           
  For example: if str is "zacxyjbbkfgtbhdaielqrm45pnsowtuv"    
  then your program should return the string true because every
  character in the alphabet exists in this string even though  
  some characters appear more than once.                       
                                                               
  Examples                                                    
  Input 1: abcdefghijklmnopqrstuvwxyyyy                        
  Output 1: false                                              
                                                               
  Input 2: abc123456kmo                                        
  Output 2: false          
"""


# Algorithm

# To solve the `AlphabetSearching` problem, we need to check whether every letter 
# of the English alphabet exists in the input string or not. We can create a set 
# of all the letters of the English alphabet and iterate over them to check if each 
# of them exists in the input string or not. If any letter is not found, we can 
# return `false`. If all letters are found, we can return `true`. Here's the Python 
# code that implements this approach:


def AlphabetSearching(str):
    alphabet = set('abcdefghijklmnopqrstuvwxyz')
    for char in alphabet:
        if char not in str:
            return "false"
    return "true"

# Test case 1: All letters are present
result1 = AlphabetSearching("zacxyjbbkfgtbhdaielqrm45pnsowtuv")
print(result1)  # Output should be "true"

# Test case 2: Some letters are missing
result2 = AlphabetSearching("abcdefhijklmnopqrstuvwxyyyy")
print(result2)  # Output should be "false"

# Test case 3: Alphanumeric input
result3 = AlphabetSearching("abc123456kmo")
print(result3)  # Output should be "false"

