"""
Problem Statement                                            
  Have the function SimpleSymbols(str) take the str parameter  
  being passed and determine if it is an acceptable sequence   
  by either returning the string true or false. The str        
  parameter will be composed of + and = symbols with several   
  characters between them (ie. ++d+===+c++==a) and for the     
  string to be true each letter must be surrounded by          
  a + symbol. So the string to the left would be false.        
  The string will not be empty & will have at least one letter 
                                                               
  Examples                                                     
  Input 1: "+d+=3=+s+"                                         
  Output 1: true                                               
                                                               
  Input 2: "f++d+"                                             
  Output 2: false          
"""
"""
Algorithm:

1. Iterate over each character, `c`, in the input string, `str`.
2. Check if `c` is a letter (using the `isalpha()` function) and if it has a preceding `+` symbol and a succeeding `+` symbol.
3. If any letter is found without the correct surrounding symbols, return `false`.
4. After the loop, if all letters have the correct surrounding symbols, return `true`.
"""
 

def SimpleSymbols(strParam):
    strParam = strParam.lower()  # Convert the input string to lowercase for case-insensitive comparison

    for i in range(len(strParam)):
        if strParam[i].isalpha():
            if i == 0 or i == len(strParam) - 1:
                return "false"  # First or last character is a letter without surrounding symbols

            if strParam[i-1] != '+' or strParam[i+1] != '+':
                return "false"  # Letter without surrounding symbols

    return "true"  # All letters have correct surrounding symbols
 

# Test case 1
print(SimpleSymbols("+d+=3=+s+"))
# Output: true

# Test case 2
print(SimpleSymbols("f++d+"))
# Output: false

# Test case 3 (Single letter surrounded by symbols)
print(SimpleSymbols("+a+"))
# Output: true

# Test case 4 (Single letter without surrounding symbols)
print(SimpleSymbols("a"))
# Output: false

# Test case 5 (Multiple letters with correct surrounding symbols)
print(SimpleSymbols("+a+b+c+d+"))
# Output: true

# Test case 6 (Symbols without any letters)
print(SimpleSymbols("+==+===+"))
# Output: true

# Test case 7 (Symbols only)
print(SimpleSymbols("+++++="))
# Output: true


