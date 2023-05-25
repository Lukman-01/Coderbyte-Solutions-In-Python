"""
Problem Statement                                            
  Have the function MissingDigit(str) take the str parameter,	
  which will be simple mathematical formula with three numbers,
  a single operator (+, -, *, or /) and an equal sign (=) and  
  return the digit that completes the equation.                
                                                               
  In one of the numbers in the equation, there will be an x    
  character, and your program should determine what digit is   
  missing.                                                     
                                                               
  For example, if str is "3x + 12 = 46" then your program      
  should output 4. The x character can appear in any of the    
  three numbers and all three numbers will be greater than or  
  equal to 0 and less than or equal to 1000000.                
                                                               
                                                               
  Examples                                                     
  Input 1: "4 - 2 = x"		                                
  Output 1: 2                                                  
                                                               
  Input 2: "1x0 * 12 = 1200"		                        
  Output 2: 0       
"""

"""
Algorithm:

1. Split the input string `str` by spaces to extract the three numbers and the operator.
2. Iterate through the split string elements to find the element that contains the 'x' character.
3. For the element containing 'x':
     - Replace the 'x' character with a placeholder digit (0-9) and convert the modified string to an integer.
     - Check if the equation holds true with the modified number.
     - If the equation is satisfied, return the placeholder digit.
4. If no solution is found, return None or any appropriate value to indicate that no missing digit was found.
"""


def MissingDigit(equation):
    num_list = equation.split()

    for i in range(len(num_list)):
        if 'x' in num_list[i]:
            for digit in range(10):
                num_list[i] = num_list[i].replace('x', str(digit))
                equation_str = ' '.join(num_list)
                if eval(equation_str):
                    return digit

    return None  # or any appropriate value to indicate no missing digit was found
 


# Test Case 1
equation = "4 - 2 = x"
print(f"Input: {equation}")
print(f"Output: {MissingDigit(equation)}")
print()

# Test Case 2
equation = "1x0 * 12 = 1200"
print(f"Input: {equation}")
print(f"Output: {MissingDigit(equation)}")
print()

# Test Case 3
equation = "5 * x = 30"
print(f"Input: {equation}")
print(f"Output: {MissingDigit(equation)}")
print()

# Test Case 4
equation = "2x + 5 = 15"
print(f"Input: {equation}")
print(f"Output: {MissingDigit(equation)}")
print()

# Test Case 5
equation = "100 / 5 = x"
print(f"Input: {equation}")
print(f"Output: {MissingDigit(equation)}")
print()
 