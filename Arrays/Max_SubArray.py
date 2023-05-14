"""
Problem Statement                                            
  Have the function MaxSubarray(arr) take the array of numbers 
  stored in arr and determine the largest sum that can be      
  formed by any contiguous subarray in the array.              
  For example, if arr is [-2, 5, -1, 7, -3] then your program  
  should return 11 because the sum is formed by the subarray   
  [5, -1, 7]. Adding any element before or after this subarray 
  would make the sum smaller.                                  
                                                               
  Examples                                                     
  Input 1: [1, -2, 0, 3]                                       
  Output 1: 3                                                  
                                                               
  Input 2: [3, -1, -1, 4, 3, -1]                               
  Output 2: 8    
"""

"""
To solve this problem, we can use Kadane's algorithm, which is an efficient 
algorithm that scans the given array containing positive and negative numbers 
and determines the maximum sum contiguous subarray.

The algorithm maintains two variables: 
- `max_so_far`: which stores the maximum sum subarray found so far.
- `max_ending_here`: which stores the maximum sum of subarray ending at the current position.

At each iteration, the algorithm calculates `max_ending_here` as the maximum 
of the current element or the sum of the current element and the `max_ending_here` 
so far. If `max_ending_here` is negative, it is set to zero. Then, it compares 
`max_so_far` with `max_ending_here` and updates `max_so_far` if `max_ending_here` is greater.

Finally, the function returns `max_so_far`.
"""


def MaxSubarray(arr):
    max_so_far = float('-inf')
    max_ending_here = 0
    for i in range(len(arr)):
        max_ending_here += arr[i]
        if max_ending_here > max_so_far:
            max_so_far = max_ending_here
        if max_ending_here < 0:
            max_ending_here = 0
    return max_so_far



print(MaxSubarray([1, -2, 0, 3]))  # Output: 3
print(MaxSubarray([3, -1, -1, 4, 3, -1]))  # Output: 8
print(MaxSubarray([5, 4, -1, 7, 8]))  # Output: 23
print(MaxSubarray([-3, -1, -2, -5, -6]))  # Output: -1
print(MaxSubarray([2, 1, -2, 3, 0, 1]))  # Output: 5