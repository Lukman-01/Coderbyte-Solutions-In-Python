"""
Problem Statement                                            
  Have the function Consecutive(arr) take the array of integers
  stored in arr and return the minimum number of integers      
  needed to make the contents of arr consecutive from the      
  lowest number to the highest number. For example: If arr     
  contains [4, 8, 6] then the output should be 2 because two   
  numbers need to be added to the array (5 and 7) to make it a 
  consecutive array of numbers from 4 to 8.                    
  Negative numbers may be entered as parameters and no array   
  will have less than 2 elements.                              
                                                               
  Examples                                                     
  Input 1: [5,10,15] 		                                
  Output 1: 8                                                  
                                                               
  Input 2: [-2,10,4]                                           
  Output 2: 10          
"""

"""
Algorithm:

1. Sort the given array `arr` in ascending order.
2. Initialize a variable `missing_count` to 0.
3. Iterate through each element `num` in the sorted array `arr` from the first index to the second-to-last index.
4. For each element `num`:
     - Calculate the difference between the next element and the current element (`arr[index+1] - arr[index] - 1`).
     - Add the difference to `missing_count`.
5. Return the value of `missing_count`.
"""


def Consecutive(arr):
    arr.sort()
    missing_count = 0
    for i in range(len(arr) - 1):
        missing_count += arr[i + 1] - arr[i] - 1
    return missing_count

# Test Case 1
arr = [5, 10, 15]
print(f"Input: {arr}")
print(f"Output: {Consecutive(arr)}")
print()

# Test Case 2
arr = [-2, 10, 4]
print(f"Input: {arr}")
print(f"Output: {Consecutive(arr)}")
print()

# Test Case 3
arr = [1, 2, 3, 4, 5]
print(f"Input: {arr}")
print(f"Output: {Consecutive(arr)}")
print()

# Test Case 4
arr = [100, 105, 110, 115, 120]
print(f"Input: {arr}")
print(f"Output: {Consecutive(arr)}")
print()

# Test Case 5
arr = [7, 5, 3, 1]
print(f"Input: {arr}")
print(f"Output: {Consecutive(arr)}")
print()
