"""
Problem Statement                                            
  Have the function LargestFour(arr) take the array of integers
  stored in arr, and find the four largest elements and return 
  their sum.                                                   
                                                               
  For example: if arr is [4, 5, -2, 3, 1, 2, 6, 6] then the    
  four largest elements in this array are 6, 6, 4, and 5 and   
  the total sum of these numbers is 21, so your program should 
  return 21.                                                   
                                                               
  If there are less than four numbers in the array your program
  should return the sum of all the numbers in the array.       
                                                               
  Examples                                                     
  Input 1: [1, 1, 1, -5]                                       
  Output 1: -2                                                 
                                                               
  Input 2: [0, 0, 2, 3, 7, 1]                                  
  Output 2: 13    
"""

"""
Type of problem: Array manipulation

Algorithm:

1. If the length of the array is less than or equal to 4, return the sum of all the elements in the array.
2. Sort the array in non-increasing order.
3. Calculate the sum of the first four elements of the sorted array.
4. Return the sum calculated in step 3.
"""


def largest_four(arr):
    n = len(arr)
    if n <= 4:
        return sum(arr)
    arr.sort(reverse=True)
    return sum(arr[:4])


print(largest_four([1, 1, 1, -5]))  #-2
print(largest_four([0, 0, 2, 3, 7, 1]))  #13
print(largest_four([4, 5, -2, 3, 1, 2, 6, 6]))  #21
print(largest_four([1, 2, 3, 4]))  #10
print(largest_four([-1, -2, -3, -4])) #-10
