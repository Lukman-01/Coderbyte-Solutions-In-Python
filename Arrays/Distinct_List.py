"""
Problem Statement                                            
  Have the function DistinctList(arr) take the array of numbers
  stored in arr and determine the total number of duplicate    
  entries. For example if the input is [1, 2, 2, 2, 3] then    
  your program should output 2 because there are two duplicates
  of one of the elements.                                      
                                                               
  Examples                                                     
  Input 1: [0,-2,-2,5,5,5]                                     
  Output 1: 3                                                  
                                                               
  Input 2: [100,2,101,4]                                       
  Output 2: 0               
"""

"""
Type of algorithm: Set-based algorithm

Algorithm outline:
1. Initialize an empty set to keep track of distinct numbers.
2. Loop through each number in the array.
3. If the number is already in the set, increment the duplicate counter.
4. If the number is not in the set, add it to the set of distinct numbers.
5. Return the duplicate counter.
"""


def DistinctList(arr):
    distinct_numbers = set()
    duplicates = 0

    for num in arr:
        if num in distinct_numbers:
            duplicates += 1
        else:
            distinct_numbers.add(num)

    return duplicates


# Test Cases
print(DistinctList([0,-2,-2,5,5,5]))  # Output: 3
print(DistinctList([100,2,101,4]))   # Output: 0
print(DistinctList([1, 2, 2, 2, 3])) # Output: 2
print(DistinctList([1, 1, 1, 1, 1])) # Output: 4
print(DistinctList([1, 2, 3, 4, 5])) # Output: 0

 