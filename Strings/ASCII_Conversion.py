"""
  Problem Statement                                            
  Have the function ASCIIConversion(str) take the str parameter
  being passed and return a new string where every character,  
  aside from the space character, is replaced with its         
  corresponding decimal character code. For example: if str is 
  "dog" then your program should return the string 100111103   
  because d = 100, o = 111, g = 103.                           

"""

# Algorithm

# 1. Define the `ASCIIConversion` function that takes a single parameter `strParam`.
# 2. Initialize an empty string called `result` to store the output.
# 3. For each character `char` in the input string `strParam`, do the following:
#    a. Check if `char` is not a space by comparing it to the string literal " ".
#    b. If `char` is not a space, use the `ord` function to get its ASCII code as an integer.
#    c. Append the string representation of the ASCII code to the `result` string using the `+=` operator.
#    d. If `char` is a space, append a space character to the `result` string using the `+=` operator.
# 4. After iterating over all characters in `str`, return the `result` string.


def ASCIIConversion(strParam):
    result = ""
    for char in strParam:
        if char != " ":
            result += str(ord(char))
        else:
            result += " "
    return result


# Test case 1: basic input
result1 = ASCIIConversion("dog")
print(result1)  # Output should be "100111103"

# Test case 2: input with spaces
result2 = ASCIIConversion("hello old")
print(result2)  # Output should be "104101108108111 111108100"

# Test case 3: input with special characters
result3 = ASCIIConversion("!@#$%^&*()")
print(result3)  # Output should be "33764235234143354642282941"

# Test case 4: input with only spaces
result4 = ASCIIConversion("     ")
print(result4)  # Output should be "     "

# Test case 5: input with no spaces
result5 = ASCIIConversion("stuvwxyz")
print(result5)  # Output should be "115116117118119120121122"
       