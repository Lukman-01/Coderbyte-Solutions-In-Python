"""
Problem Statement                                            
  Have the function FormattedDivision(num1,num2) take both     
  parameters being passed, divide num1 by num2, and return the 
  result as a string with properly formatted commas and 4      
  significant digits after the decimal place.                   
                                                               
  For example: if num1 is 123456789 and num2 is 10000          
  the output should be "12,345.6789".                          
  The output must contain a number in the one's place even     
  if it is a zero.                                             
                                                               
  Examples                                                     
  Input 1: 2 and 3                                             
  Output 1: 0.6667                                             
                                                               
  Input 2: 10 and 10                                           
  Output 2: 1.0000       
"""

"""
                                            Algorithm:

1. Divide `num1` by `num2` to get the result.
2. Format the result using `format()` function with `,` separator and `:.4f` to get 4 significant digits after the decimal place.
3. Return the formatted result.
"""
                            
def FormattedDivision(num1, num2):
    result = num1 / num2
    formatted_result = '{:,.4f}'.format(result)
    return formatted_result

# Test case 1: basic input
result1 = FormattedDivision(123456789, 10000)
print(result1)  # Output should be "12,345.6789"

# Test case 2: input with zeros
result2 = FormattedDivision(2, 3)
print(result2)  # Output should be "0.6667"

# Test case 3: input with no decimals
result3 = FormattedDivision(10, 10)
print(result3)  # Output should be "1.0000"
