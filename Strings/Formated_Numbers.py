"""
Problem Statement                                            
  Have the function FormattedNumber(strArr) take the strArr    
  parameter being passed, which will only contain a single     
  element, and return the string true if it is a valid number  
  that contains only digits with properly placed decimals &    
  commas, otherwise return the string false.                   
  For example: if strArr is ["1,093,222.04"] then your program 
  should return the string true, but if the input were         
  ["1,093,22.04"] then your program should return the string   
  false. The input may contain characters other than digits.   
                                                               
  Examples                                                     
  Input 1: ["0.232567"]                                        
  Output 1: true                                               
                                                               
  Input 2: ["2,567.00.2"]                                      
  Output 2: false          
"""
"""
Algorithm:
1. Remove all commas from the string.
2. Count the number of decimal points in the string.
3. If there are more than one decimal points or more than one '-' sign, return false.
4. If there is one decimal point, then split the string at that decimal point. Check that the left side is only digits, and the right side is only digits and has 2 or fewer characters.
5. If there is no decimal point, check that the entire string is only digits.

"""

def FormattedNumber(strArr):
    # Get the input string from strArr
    input_string = strArr[0]
    
    # Remove all commas from the input string
    input_string = input_string.replace(",", "")
    
    # Split the input string into two parts by the decimal point
    parts = input_string.split(".")
    
    # Check that there are at most two parts, and that each part consists only of digits
    if len(parts) > 2 or not all(part.isdigit() for part in parts):
        return "false"
    
    # If there are two parts, check that the second part has no more than two digits
    if len(parts) == 2 and len(parts[1]) > 2:
        return "false"
    
    # Otherwise, the input is a properly formatted number
    return "true"



# Test case 1
input1 = ["0.232567"]
output1 = FormattedNumber(input1)
print(output1)  # Expected output: true

# Test case 2
input2 = ["2,567.00.2"]
output2 = FormattedNumber(input2)
print(output2)  # Expected output: false

# Test case 3
input3 = ["123,456,789"]
output3 = FormattedNumber(input3)
print(output3)  # Expected output: true

# Test case 4
input4 = ["$1,234.56"]
output4 = FormattedNumber(input4)
print(output4)  # Expected output: false



 