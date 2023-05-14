"""
Problem Statement                                            
  Have the function ArrayRotation(arr) take the arr parameter  
  being passed which will be an array of non-negative integers 
  and circularly rotate the array starting from the Nth        
  element where N is equal to the first integer in the array.  
                                                               
  For example: if arr is [2, 3, 4, 1, 6, 10] then your program 
  should rotate the array starting from the 2nd position       
  because the first element in the array is 2.                 
  The final array will therefore be [4, 1, 6, 10, 2, 3], and   
  your program should return the new array as a string, so for 
  this example your program would return 4161023.              
  The first element in the array will always be an integer     
  greater than or equal to 0 & less than the size of the array 
                                                               
  Examples                                                     
  Input 1: [3,2,1,6]                                           
  Output 1: 6321                                               
                                                               
  Input 2: [4,3,4,3,1,2]                                       
  Output 2: 124343     
"""

"""
Algorithm:
1. Store the first element of the array in a variable "rot".
2. Rotate the array starting from the (rot+1)th position to the end of the array.
3. Append the first "rot" elements of the original array to the end of the rotated array.
4. Return the rotated array as a string.
"""
 

def ArrayRotation(arr):
  n = arr[0]
  rotated = arr[n:] + arr[:n]
  return "".join(str(x) for x in rotated)


Input1 = [3,2,1,6]
print(ArrayRotation(Input1))

Input2 = [4,3,4,3,1,2]
print(ArrayRotation(Input2))

Input3 = [0,1,2,3,4,5]
print(ArrayRotation(Input3))

Input4 = [5,4,3,2,1,0]
print(ArrayRotation(Input4))

Input5 = [1,2,3,4,5,0]
print(ArrayRotation(Input5))
