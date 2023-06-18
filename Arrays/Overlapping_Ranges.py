"""
 Problem Statement                                            
  Have the function OverlappingRanges(arr) take the array of   
  numbers stored in arr which will contain 5 positive integers,
  the first two representing a range of numbers (a to b), the  
  next 2 also representing another range of integers (c to d), 
  and a final 5th element (x) which will also be a positive    
  integer, and return the string true if both sets of ranges   
  overlap by at least x numbers.                               
  For example: if arr is [4, 10, 2, 6, 3] then your program    
  should return the string true.                               
  The first range of numbers are 4, 5, 6, 7, 8, 9, 10 & the    
  second range of numbers are 2, 3, 4, 5, 6.                   
  The last element in the array is 3, and there are 3 numbers  
  that overlap between both ranges: 4, 5, and 6.               
  If both ranges do not overlap by at least x numbers,         
  then your program should return the string false.            
                                                               
  Examples                                                     
  Input 1: [5,11,1,5,1]                                        
  Output 1: true                                               
                                                               
  Input 2: [1,8,2,4,4]                                         
  Output 2: false           
"""

# Algorithm

# 1. Extract the values from the input array `arr` and assign them to variables:
#    - Set `a` as the first element of `arr`.
#    - Set `b` as the second element of `arr`.
#    - Set `c` as the third element of `arr`.
#    - Set `d` as the fourth element of `arr`.
#    - Set `x` as the fifth element of `arr`.

# 2. Determine the overlapping range:
#    - Calculate the start of the overlapping range as the maximum of `a` and `c`.
#    - Calculate the end of the overlapping range as the minimum of `b` and `d`.

# 3. Calculate the number of overlapping numbers by subtracting the start of the overlapping range from the end of the overlapping range and adding 1.

# 4. If the number of overlapping numbers is greater than or equal to `x`, return the string "true". Otherwise, return the string "false".

 
def OverlappingRanges(arr):
    a, b, c, d, x = arr
    
    start = max(a, c)
    end = min(b, d)
    
    overlap_count = end - start + 1
    
    if overlap_count >= x:
        return "true"
    else:
        return "false"
 
# Test case 1: Both ranges overlap by exactly x numbers
print(OverlappingRanges([4, 10, 2, 6, 3]))  # Output: true

# Test case 2: Both ranges do not overlap
print(OverlappingRanges([1, 8, 2, 4, 4]))  # Output: false

# Test case 3: Both ranges overlap by more than x numbers
print(OverlappingRanges([1, 10, 5, 15, 6]))  # Output: true

# Test case 4: Both ranges overlap by less than x numbers
print(OverlappingRanges([1, 5, 6, 10, 4]))  # Output: false

# Test case 5: Both ranges overlap at one number only
print(OverlappingRanges([1, 3, 2, 4, 2]))  # Output: true
 