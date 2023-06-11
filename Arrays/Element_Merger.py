"""
Problem Statement                                            
  Have the function ElementMerger(arr) take the array of       
  positive integers stored in arr and perform the following    
  algorithm: continuously get the difference of adjacent       
  integers to create a new array of integers, then do the same 
  for the new array until a single number is left and return   
  that number.                                                 
                                                               
  For example: if arr is [4, 5, 1, 2, 7] then taking the       
  difference of each pair of elements produces the following   
  new array: [1, 4, 1, 5]. Then do the same for this new array 
  to produce [3, 3, 4] -> [0, 1] -> 1. So for this example your
  program should return the number 1 because that is what's    
  left at the end.                                             
                                                               
  Examples                                                     
  Input 1: [5, 7, 16, 1, 2]                                    
  Output 1: 7                                                  
                                                               
  Input 2: [1, 1, 1, 2]                                        
  Output 2: 1   
"""

# 1. Initialize a variable `new_arr` and set it as a copy of the input array `arr`.
# 2. While the length of `new_arr` is greater than 1, do the following:
#      - Create an empty list called `temp`.
#      - Iterate over the range from 1 to the length of `new_arr`:
#          - Calculate the difference between `new_arr[i]` and `new_arr[i-1]`.
#          - Append the difference to `temp`.
#      - Set `new_arr` as a copy of `temp`.
# 3. Return the single number left in `new_arr`.

 
def ElementMerger(arr):
  new_arr = arr.copy()
  while len(new_arr) > 1:
    temp = []
    for i in range(1, len(new_arr)):
      diff = abs(new_arr[i] - new_arr[i-1])
      temp.append(diff)
    new_arr = temp.copy()
  return new_arr[0]
 
    
# Test case 1
arr = [5, 7, 16, 1, 2]
print(ElementMerger(arr))
# Output: 7

# Test case 2
arr = [1, 1, 1, 2]
print(ElementMerger(arr))
# Output: 1

# Test case 3
arr = [4, 5, 1, 2, 7]
print(ElementMerger(arr))
# Output: 1

# Test case 4
arr = [10, 5, 8, 3, 2]
print(ElementMerger(arr))
# Output: 2

# Test case 5
arr = [3, 3, 3, 3, 3, 3, 3, 3]
print(ElementMerger(arr))
# Output: 0
 