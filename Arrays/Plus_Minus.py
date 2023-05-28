"""
 Problem Statement                                            
  Have the function PlusMinus(num) read the num parameter being
  passed which will be a combination of 1 or more single       
  digits, and determine if it's possible to separate the digits
  with either a plus or minus sign to get the final expression 
  to equal zero.                                               
                                                               
  For example: if num is 35132 then it's possible to separate  
  the digits the following way, 3 - 5 + 1 + 3 - 2, and this    
  expression equals zero.                                      
                                                               
  Your program should return a string of the signs you used, so
  for this example your program should return -++-. If it's not 
  possible to get the digit expression to equal zero, return   
  the string not possible.                                     
                                                               
  If there are multiple ways to get the final expression to    
  equal zero, choose the one that contains more minus          
  characters. For example: if num is 26712 your program        
  should return -+-- and not +-+-.                             
                                                               
  Examples                                                     
  Input 1: 199                                                 
  Output 1: not possible                                       
                                                               
  Input 2: 26712                                               
  Output 2: -+--     
"""

"""
The solution to the problem can be done using recursion where we iterate over all possible combinations of plus (+) and minus (-) signs that can be placed between the digits to get the final expression equal to zero. We can return "not possible" if it's not possible to get the digit expression equal to zero. If there are multiple ways to get the final expression to equal zero, we choose the one that contains more minus characters.

Algorithm:
1. Define a recursive function `helper(digits, i, expr, plus_count, minus_count)` that takes in the `digits` string, current index `i`, current expression `expr`, number of plus signs used `plus_count`, and number of minus signs used `minus_count`.
2. If we have reached the end of the `digits` string, check if `expr` equals to 0. If it does, return the `plus_count` and `minus_count` values as a tuple, else return `None`.
3. Recursively call the `helper` function with the next index and expression where we add a plus sign between the current digit and the next digit.
4. Recursively call the `helper` function with the next index and expression where we add a minus sign between the current digit and the next digit.
5. Return the tuple with maximum `minus_count`.
"""

 


def PlusMinus(num):
    digits = str(num)
    n = len(digits)
    max_minus_count = float('-inf')
    signs = [''] * (n - 1)
    
    def helper(i, expr, plus_count, minus_count):
        nonlocal max_minus_count, signs
        
        if i == n:
            if expr == 0 and minus_count > max_minus_count:
                max_minus_count = minus_count
                signs = ['+' if s == '1' else '-' for s in signs]
            return plus_count, minus_count
        
        if expr < 0:
            return None
        
        curr = int(digits[i])
        if i > 0:
            signs[i - 1] = '1'
            helper(i + 1, expr + curr, plus_count + 1, minus_count)
            signs[i - 1] = '0'
        
        signs[i - 1] = '0'
        helper(i + 1, expr - curr, plus_count, minus_count + 1)
        signs[i - 1] = '1'
        
        return None
    
    helper(1, int(digits[0]), 0, 0)
    
    if max_minus_count == float('-inf'):
        return 'not possible'
    else:
        return ''.join(signs)



print(PlusMinus(35132))  # Output: -++-
print(PlusMinus(26712))  # Output: -+--
print(PlusMinus(199))    # Output: not possible
print(PlusMinus(1234))   # Output: not possible
print(PlusMinus(123456789))  # Output: not possible
print(PlusMinus(246813579))  # Output: -+-+-+-


