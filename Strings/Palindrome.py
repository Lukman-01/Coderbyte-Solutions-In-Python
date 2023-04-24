"""
Problem Statement                                            
  Have the function Palindrome(str) take the str parameter     
  being passed and return the string true if the parameter is  
  a palindrome, (the string is the same forward as it is       
  backward) otherwise return the string false. For example:    
  "racecar" is also "racecar" backwards. Punctuation & numbers 
  will not be part of the string.                              
                                                               
  Examples                                                     
  Input 1: never odd or even                                   
  Output 1: true                                               
                                                               
  Input 2: eye                                                 
  Output 2: true      
"""
"""
                                Agorithm 
1. Remove all non-alphabetic characters and convert the string to lowercase.

2. Reverse the string.

3. Compare the original string with the reversed string.

4. If they are the same, return "true". Otherwise, return "false".

"""
def Palindrome(strParam):
    # Remove non-alphabetic characters and convert to lowercase
    strParam = "".join(ch.lower() for ch in strParam if ch.isalpha())

    # Reverse the string
    rev_str = strParam[::-1]

    # Compare original string with reversed string
    if strParam == rev_str:
        return "true"
    else:
        return "false"

# Test case 1: basic input
result1 = Palindrome("never odd or even")
print(result1)  # Output should be "true"

# Test case 2: input with a single letter
result2 = Palindrome("a")
print(result2)  # Output should be "true"

# Test case 3: input with numbers and special characters
result3 = Palindrome("A man, a plan, a canal: Panama")
print(result3)  # Output should be "true"

# Test case 4: input with uppercase letters
result4 = Palindrome("Was it a car or a cat I saw?")
print(result4)  # Output should be "true"

# Test case 5: input that is not a palindrome
result5 = Palindrome("hello world")
print(result5)  # Output should be "false"
