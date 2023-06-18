"""
Problem Statement                                            
  Have the function SecondGreatLow(arr) take the array of      
  numbers stored in arr and return the second lowest and second
  greatest numbers, respectively, separated by a space.        
  For example: if arr contains [7, 7, 12, 98, 106] the output  
  should be 12 98. The array will not be empty and will contain
  at least 2 numbers. It can get tricky if there's just        
  two numbers!                                                 
                                                            
  Examples                                                     
  Input 1: new int[] {1, 42, 42, 180}                          
  Output 1: 42 42                                              
                                                               
  Input 2: new int[] {4, 90}                                   
  Output 2: 90 4       
"""

# Algorithm 

# 1. Remove any duplicate numbers from the array to ensure that we have a distinct set of numbers.

# 2. Sort the array in ascending order.

# 3. Check if the length of the array is 2.
#    - If it is, return the second number followed by the first number.

# 4. Otherwise, return the second number and the second-to-last number in the sorted array, separated by a space.

 


def SecondGreatLow(arr):
    distinct_arr = list(set(arr))  # Remove duplicates
    sorted_arr = sorted(distinct_arr)  # Sort in ascending order

    if len(sorted_arr) == 2:
        return str(sorted_arr[1]) + " " + str(sorted_arr[0])
    else:
        return str(sorted_arr[1]) + " " + str(sorted_arr[-2])
 

# Test case 1: Multiple occurrences of the second lowest and second greatest numbers
print(SecondGreatLow([1, 42, 42, 180]))  # Output: 42 42

# Test case 2: Only two numbers in the array
print(SecondGreatLow([4, 90]))  # Output: 90 4

# Test case 3: Array with distinct numbers
print(SecondGreatLow([7, 7, 12, 98, 106]))  # Output: 12 98

# Test case 4: Array with negative numbers
print(SecondGreatLow([-5, -2, -10, -8, -3]))  # Output: -8 -3

# Test case 5: Array with duplicate numbers and negative numbers
print(SecondGreatLow([100, -20, 50, -20, 10]))  # Output: 10 50
