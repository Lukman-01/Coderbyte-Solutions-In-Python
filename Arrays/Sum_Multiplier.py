"""
Problem Statement                                            
  Have the function SumMultiplier(arr) take the array of      
  numbers stored in arr and return the string true if any two  
  numbers can be multiplied so that the answer is greater than 
  double the sum of all the elements in the array. If not,     
  return the string false.                                     
  For example: if arr is [2, 5, 6, -6, 16, 2, 3, 6, 5, 3] then 
  the sum of all these elements is 42 and doubling it is 84.   
  There are two elements in the array, 16 * 6 = 96 and 96 is   
  greater than 84 so your program should return the string true
                                                               
  Examples                                                     
  Input 1: [2, 2, 2, 2, 4, 1]                                  
  Output 1: false                                              
                                                               
  Input 2: [1, 1, 2, 10, 3, 1, 12]                             
  Output 2: true        
"""

# Algorithm

# 1. Calculate the sum of all elements in the array and store it in a variable named `total_sum`.

# 2. Calculate the double of the `total_sum` and store it in a variable named `double_sum`.

# 3. Sort the array in descending order.

# 4. Iterate through the sorted array and for each number `num`, starting from the first element:
#    - Multiply `num` by the next number in the array.
#    - If the result is greater than `double_sum`, return the string "true" as there exists a pair of numbers that can be multiplied to exceed the double sum.

# 5. If the loop completes without finding a pair of numbers that satisfies the condition, return the string "false".


def SumMultiplier(arr):
    total_sum = sum(arr)
    double_sum = total_sum * 2

    sorted_arr = sorted(arr, reverse=True)

    for i in range(len(sorted_arr) - 1):
        if sorted_arr[i] * sorted_arr[i+1] > double_sum:
            return "true"

    return "false"
 


# Test case 1: No pair of numbers can be multiplied to exceed the double sum
print(SumMultiplier([2, 2, 2, 2, 4, 1]))  # Output: false

# Test case 2: Pair of numbers (12 and 10) can be multiplied to exceed the double sum
print(SumMultiplier([1, 1, 2, 10, 3, 1, 12]))  # Output: true

# Test case 3: No pair of numbers can be multiplied to exceed the double sum
print(SumMultiplier([1, 2, 3, 4, 5]))  # Output: false

# Test case 4: Pair of numbers (16 and 6) can be multiplied to exceed the double sum
print(SumMultiplier([2, 5, 6, -6, 16, 2, 3, 6, 5, 3]))  # Output: true

# Test case 5: Pair of numbers (50 and 25) can be multiplied to exceed the double sum
print(SumMultiplier([10, 20, 30, 40, 50, 25]))  # Output: true
