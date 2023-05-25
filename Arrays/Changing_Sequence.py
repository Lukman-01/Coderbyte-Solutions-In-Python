"""
Problem Statement                                            
  Have the function ChangingSequence(arr) take the array of    
  numbers stored in arr and return the index at which the      
  numbers stop increasing and begin decreasing or stop         
  decreasing and begin increasing.                             
  For example: if arr is [1, 2, 4, 6, 4, 3, 1] then your       
  program should return 3 because 6 is the last point in the   
  array where the numbers were increasing and the next number  
  begins a decreasing sequence. The array will contain at least
  3 numbers and it may contains only a single sequence,        
  increasing or decreasing. If there is only a single sequence 
  in the array, then your program should return -1.            
  Indexing should begin with 0.                                
                                                               
  Examples                                                     
  Input 1: [-4, -2, 9, 10]                                     
  Output 1: -1                                                 
                                                               
  Input 2: [5, 4, 3, 2, 10, 11]                                
  Output 2: 3             
"""

"""
Algorithm:

1. Initialize a variable `direction` to track the sequence direction. Set it to `None`.
2. Iterate through the array `arr` starting from index 1:
     - If `direction` is `None`, compare the current element with the previous element.
       - If they are equal, continue to the next iteration.
       - If the current element is greater than the previous element, set `direction` to `'increasing'`.
       - If the current element is less than the previous element, set `direction` to `'decreasing'`.
     - If `direction` is `'increasing'`, check if the current element is less than or equal to 
        the previous element. If true, return the current index minus 1.
     - If `direction` is `'decreasing'`, check if the current element is greater than 
        or equal to the previous element. If true, return the current index minus 1.
3. If the loop completes without returning, return -1 to indicate that there is only a single sequence in the array.
"""
 

def ChangingSequence(arr):
    direction = None

    for i in range(1, len(arr)):
        if direction is None:
            if arr[i] == arr[i-1]:
                continue
            elif arr[i] > arr[i-1]:
                direction = 'increasing'
            else:
                direction = 'decreasing'
        elif direction == 'increasing':
            if arr[i] <= arr[i-1]:
                return i - 1
        elif direction == 'decreasing':
            if arr[i] >= arr[i-1]:
                return i - 1
    
    return -1
 
    
print(ChangingSequence([-4, -2, 9, 10]))   # Output: -1
print(ChangingSequence([5, 4, 3, 2, 10, 11]))   # Output: 3
print(ChangingSequence([1, 2, 4, 6, 4, 3, 1]))   # Output: 3
print(ChangingSequence([1, 2, 3, 4, 5, 6]))   # Output: -1
print(ChangingSequence([9, 8, 7, 6, 5, 4]))   # Output: -1
 