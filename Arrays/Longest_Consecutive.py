"""
Problem Statement                                            
  Have the function LongestConsecutive(arr) take the array of  
  positive integers stored in arr and return the length of the 
  longest consecutive subsequence (LCS).                       
  An LCS is a subset of the original list where the numbers    
  are in sorted order, from lowest to highest, and are in a    
  consecutive, increasing order. The sequence does not need to 
  be contiguous and there can be several different subsequences
                                                               
  For example: if arr is [4, 3, 8, 1, 2, 6, 100, 9] then a few 
  consecutive sequences are [1, 2, 3, 4], and [8, 9].          
  For this input, your program should return 4 because that is 
  the length of the longest consecutive subsequence.           
                                                               
  If there are less than four numbers in the array your program
  should return the sum of all the numbers in the array.       
                                                               
  Examples                                                     
  Input 1: [6, 7, 3, 1, 100, 102, 6, 12]                       
  Output 1: 2                                                  
                                                               
  Input 2: [5, 6, 1, 2, 8, 9, 7]                               
  Output 2: 5   
"""
"""
Type of problem: Array manipulation

Algorithm:

1. Create an empty set to store the numbers.
2. Add all the numbers in the array to the set.
3. Initialize a variable `longest_sequence` to 0.
4. For each number in the array, check if it is the start of a new 
    consecutive sequence by verifying if `number-1` is in the set.
5. If the number is the start of a new consecutive sequence, 
    keep incrementing a counter until the end of the sequence is reached.
6. Update the `longest_sequence` variable if the counter exceeds its value.
7. Return the `longest_sequence` variable.
"""


def longest_consecutive(arr):
    nums = set(arr)
    longest_sequence = 0
    for num in nums:
        if num-1 not in nums:
            current_sequence = 1
            while num+1 in nums:
                current_sequence += 1
                num += 1
            longest_sequence = max(longest_sequence, current_sequence)
    return longest_sequence
 

print(longest_consecutive([6, 7, 3, 1, 100, 102, 6, 12])) #== 2
print(longest_consecutive([5, 6, 1, 2, 8, 9, 7])) #== 5
print(longest_consecutive([4, 3, 8, 1, 2, 6, 100, 9])) #== 4
print(longest_consecutive([1, 2, 3, 4])) #== 4
print(longest_consecutive([5, 4, 3, 2, 1])) #== 5

