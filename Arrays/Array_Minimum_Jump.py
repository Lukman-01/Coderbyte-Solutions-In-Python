"""
Problem Statement                                            
  Have the function ArrayMinJumps(arr) take the array of       
  integers stored in arr, where each integer represents the    
  maximum number of steps that can be made from that position, 
  and determine the least amount of jumps that can be made to  
  reach the end of the array.                                  
  For example: if arr is [1, 5, 4, 6, 9, 3, 0, 0, 1, 3] then   
  your program should output the number 3 because you can reach
  the end of the array from the beginning via the following    
  steps: 1 -> 5 -> 9 -> END or 1 -> 5 -> 6 -> END.             
  Both of these combinations produce a series of 3 steps.      
  And as you can see, you don't always have to take the maximum
  number of jumps at a specific position, you can take less    
  jumps even though the number is higher.                      
                                                               
  If it's not possible to reach the end of the array, return -1
                                                               
  Examples                                                     
  Input 1: [3, 4, 2, 1, 1, 100]                                
  Output 1: 2                                                  
                                                               
  Input 2: [1, 3, 6, 8, 2, 7, 1, 2, 1, 2, 6, 1, 2, 1, 2]       
  Output 2: 4           
"""

"""
Algorithm:

1. Initialize a variable called jumps to 0 and variables called current_end and farthest to 0.
2. Iterate through each integer in the array:
   a. If the sum of the current index and the integer at that index is greater than or equal to the length of the array minus 1, return jumps + 1 because that means the end of the array can be reached with one more jump.
   b. Otherwise, update farthest to the maximum value of farthest and the sum of the current index and the integer at that index.
   c. If the current index is equal to current_end, update current_end to farthest and increment jumps by 1.
3. If current_end is less than or equal to the current index, return -1 because the end of the array cannot be reached.

"""

def ArrayMinJumps(arr):
  jumps = 0
  current_end = 0
  farthest = 0
  for i in range(len(arr)):
    if i + arr[i] >= len(arr) - 1:
      return jumps + 1
    farthest = max(farthest, i + arr[i])
    if i == current_end:
      current_end = farthest
      jumps += 1
    if current_end <= i:
      return -1
 

Input1= [3, 4, 2, 1, 1, 100]
print(ArrayMinJumps(Input1)) #2

Input2= [1, 3, 6, 8, 2, 7, 1, 2, 1, 2, 6, 1, 2, 1, 2]
print(ArrayMinJumps(Input2)) #4

Input3= [1, 0, 1, 0, 1, 0, 1, 0]
print(ArrayMinJumps(Input3)) #-1

Input4= [1, 1, 1, 1, 1, 1, 1, 1]
print(ArrayMinJumps(Input4)) #7

Input5= [5, 4, 3, 2, 1, 0]
print(ArrayMinJumps(Input5)) #1
