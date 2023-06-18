"""
Problem Statement                                            
  Have the function ThirdGreatest(strArr) take the array of    
  strings stored in strArr and return the third largest word   
  within it. So For Example:                                   
  if strArr is ["hello", "world", "before", "all"] your output 
  should be world because "before" is 6 letters long,          
  and "hello" and "world" are both 5, but the output should be 
  world because it appeared as the last 5 letter word in the   
  array. If strArr was ["hello", "world", "after", "all"] the  
  output should be after because the first three words are all 
  5 letters long, so return the last one. The array will have  
  at least three strings and each string will only contain     
  letters.                                                    
                                                               
  Examples                                                     
  Input 1: new string[] {"coder","byte","code"}                
  Output 1: code                                               
                                                               
  Input 2: new string[] {"abc","defg","z","hijk"}              
  Output 2: abc                            
"""

# Algorithm

# 1. Sort the `strArr` in descending order based on the length of the strings. If multiple strings have the same length, the order of appearance should be maintained.

# 2. Return the string at the index `2` (the third largest word) from the sorted array.

 


def ThirdGreatest(strArr):
    sorted_arr = sorted(strArr, key=len, reverse=True)
    return sorted_arr[2]
 


# Test case 1: Return the third largest word with different lengths
print(ThirdGreatest(["hello", "world", "before", "all"]))  # Output: world

# Test case 2: Return the third largest word with the same lengths
print(ThirdGreatest(["hello", "world", "after", "all"]))  # Output: after

# Test case 3: Return the third largest word with repeated lengths
print(ThirdGreatest(["coder", "byte", "code"]))  # Output: code

# Test case 4: Return the third largest word with the same length as others
print(ThirdGreatest(["abc", "defg", "z", "hijk"]))  # Output: abc

# Test case 5: Return the third largest word with varying lengths
print(ThirdGreatest(["programming", "is", "fun", "and", "challenging"]))  # Output: challenging
