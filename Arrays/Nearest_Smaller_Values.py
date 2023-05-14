"""
Problem Statement                                            
  Have the function NearestSmallerValues(arr) take the array of
  integers stored in arr, and for each element in the list,    
  search all the previous values for the nearest element that  
  is smaller than (or equal to) the current element and create 
  a new list from these numbers. If there is no element before 
  a certain position that is smaller, input a -1.              
  For example: if arr is [5, 2, 8, 3, 9, 12] then the nearest  
  smaller values list is [-1, -1, 2, 2, 3, 9].                 
  The logic is as follows: For 5, there is no smaller previous 
  value so the list so far is [-1]. For 2, there is also no    
  smaller previous value, so the list is now [-1, -1].         
  For 8, the nearest smaller value is 2 so the list is now     
  [-1, -1, 2]. For 3, the nearest smaller value is also 2,     
  so the list is now [-1, -1, 2, 2]. This goes on to produce   
  the answer above. Your program should take this final list   
  and return the elements as a string separated by a           
  space: -1 -1 2 2 3 9                                         
                                                               
  Examples                                                     
  Input 1: [5, 3, 1, 9, 7, 3, 4, 1]                            
  Output 1: -1 -1 -1 1 1 1 3 1                                 
                                                               
  Input 2: [2, 4, 5, 1, 7]                                     
  Output 2: -1 2 4 -1 1                                   
"""

"""
The algorithm used in the code is as follows:
1. Initialize an empty list called `result`.
2. Loop through the input list `arr` and for each element, perform the following steps:
   a. Set `j` equal to `i-1`.
   b. Loop through the elements of `arr` from the current index `j` to 0 in reverse order.
   c. If the element at index `j` is less than the current element at index `i`, 
    append the element at index `j` to `result` and break out of the loop.
   d. If the loop finishes without finding a smaller element, append "-1" to `result`.
3. Convert `result` to a string separated by spaces using the `join` method and return the resulting string.
"""

# def NearestSmallerValues(arr):
#     stack = []
#     result = []
#     for i in range(len(arr)):
#         while stack and arr[i] <= stack[-1][0]:
#             stack.pop()
#         if not stack:
#             result.append("-1")
#         else:
#             result.append(str(stack[-1][1]))
#         stack.append((arr[i], i))
#     return " ".join(result)


def NearestSmallerValues(arr):
    n = len(arr)
    result = []
    for i in range(n):
        j = i - 1
        while j >= 0:
            if arr[j] < arr[i]:
                result.append(str(arr[j]))
                break
            j -= 1
        if j < 0:
            result.append("-1")
    return " ".join(result)

    
print(NearestSmallerValues([5, 2, 8, 3, 9, 12]))  # "-1 -1 2 2 3 9"
print(NearestSmallerValues([5, 3, 1, 9, 7, 3, 4, 1]))  # "-1 -1 -1 1 1 1 3 1"
print(NearestSmallerValues([2, 4, 5, 1, 7]))  # "-1 2 4 -1 1"
print(NearestSmallerValues([10, 4, 6, 12, 5, 9, 8]))  # "-1 -1 4 6 4 5 5"
