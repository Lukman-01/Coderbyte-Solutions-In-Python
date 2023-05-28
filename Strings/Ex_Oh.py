"""
Problem Statement                                            
  Have the function ExOh(str) take the str parameter being     
  passed & return the string true if there is an equal number  
  of x's & o's, otherwise return the string false. Only these  
  two letters will be entered in the string, no punctuation or 
  numbers. For example: if str is "xooxxxxooxo" then the       
  output should return false because there are 6 x's and 5 o's 
                                                               
  Examples                                                     
  Input 1: xooxxo                                              
  Output 1: true                                               
                                                               
  Input 2: x                                                   
  Output 2: false   
"""

# Algorithm
# 1. Define a function called ExOh that takes a string argument called "str"
# 2. Initialize two variables, "x_count" and "o_count", to 0
# 3. Loop through each character in "str"
# 4. If the current character is "x", increment "x_count" by 1
# 5. If the current character is "o", increment "o_count" by 1
# 6. After the loop, compare "x_count" and "o_count"
# 7. If they are equal, return the string "true"
# 8. If they are not equal, return the string "false"

 
def ExOh(str):
    count_x = 0
    count_o = 0
    for ch in str:
        if ch == 'x':
            count_x += 1
        elif ch == 'o':
            count_o += 1
    return count_x == count_o


print(ExOh('xooxxo'))  # Output: True
print(ExOh('x'))       # Output: False
print(ExOh('xo'))       # Output: True
print(ExOh('oxo'))      # Output: False
print(ExOh('xxxxoooo')) # Output: True
print(ExOh('xxxxoooox'))# Output: False
