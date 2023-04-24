"""
Problem Statement                                            
  Have the function FirstReverse(str) take the str parameter   
  being passed and return the string in reversed order.        
                                                               
  Test Cases                                                   
  For example: if the input string is "Hello World and Coders" 
  then your program should return the string                   
  sredoC dna dlroW olleH.                                      
                                                               
  Examples                                                     
  Input 1: coderbyte                                           
  Output 1: etybredoc                                          
                                                               
  Input 2: I Love Code                                         
  Output 2: edoC evoL I   
"""  
"""
                                Algorithm

1. Initialize an empty string `result`.

2. Loop through each character in the input string `str`, 
starting from the end of the string and moving towards the beginning.

3. Append each character to the `result` string.

4. Return the `result` string.

"""

def FirstReverse(strParam):
    result = ""
    for i in range(len(strParam) - 1, -1, -1):
        result += strParam[i]
    return result

# Test case 1: basic input
result1 = FirstReverse("Hello World and Coders")
print(result1)  # Output should be "sredoC dna dlroW olleH"

# Test case 2: input with spaces and capital letters
result2 = FirstReverse("I Love Code")
print(result2)  # Output should be "edoC evoL I"

# Test case 3: input with punctuation
result3 = FirstReverse("coderbyte")
print(result3)  # Output should be "etybredoc"

# Test case 4: input with repeated characters
result4 = FirstReverse("eeeeeee")
print(result4)  # Output should be "eeeeeee"

# Test case 5: input with a single character
result5 = FirstReverse("Lukman")
print(result5)  # Output should be "x"
