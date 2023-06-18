"""
Problem Statement                                            
  Have the function Superincreasing(arr) take the array of     
  numbers stored in arr and determine if the array forms a     
  superincreasing sequence where each element in the array is  
  greater than the sum of all previous elements. The array will
  only consist of positive integers.                           
  For example: if arr is [1, 3, 6, 13, 54] then your program   
  should return the string "true" because it forms a           
  superincreasing sequence. If a superincreasing sequence      
  isn't formed, then your program should return the string     
  "false"                                                      
                                                               
  Examples                                                     
  Input 1: [1,2,3,4]                                           
  Output 1: false                                              
                                                               
  Input 2: [1,2,5,10]                                          
  Output 2: true        
"""

# Algorithm 

# 1. Initialize a variable `sum_so_far` to 0, which will keep track of the running sum of the previous elements.

# 2. Iterate through the array, starting from the first element:
#    - If the current element is less than or equal to `sum_so_far`, return "false" since it violates the superincreasing condition.
#    - Otherwise, update `sum_so_far` by adding the current element to it.

# 3. If the loop completes without returning "false", return "true" since the array forms a superincreasing sequence.

 

 
def Superincreasing(arr):
    sum_so_far = 0

    for num in arr:
        if num <= sum_so_far:
            return "false"
        sum_so_far += num

    return "true"
 

# Test case 1: Elements in the array are not greater than the sum of previous elements
print(Superincreasing([1, 2, 3, 4]))  # Output: false

# Test case 2: Elements in the array are greater than the sum of previous elements
print(Superincreasing([1, 2, 5, 10]))  # Output: true
