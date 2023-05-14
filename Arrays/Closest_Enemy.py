"""
 Problem Statement                                            
  Have the function ClosestEnemy(arr) take the array of numbers
  stored in arr and from the position in the array where a 1	
  is, return the number of spaces either left or right you	
  must move to reach an enemy which is represented by a 2.	
  For example: if arr is [0, 0, 1, 0, 0, 2, 0, 2] then your	
  program should return 3 because the closest enemy (2) is 3	
  spaces away from the 1. The array will contain any number of	
  0's and 2's, but only a single 1. It may not contain any 2's	
  at all as well, where in that case your program should	
  return a 0. 							
                                                               
  Examples                                                     
  Input 1: [1, 0, 0, 0, 2, 2, 2] 	                        
  Output 1: 4                                                  
                                                               
  Input 2: [2, 0, 0, 0, 2, 2, 1, 0]                            
  Output 2: 1             
"""

"""
To solve the problem, we need to find the index of 1 in the array and then iterate over the array to find the index of the closest 2 either to the left or right of the index of 1. We can keep track of the minimum distance to a 2 and return it as the output. If there are no 2's in the array, we can return 0 as the output.

Algorithm:
1. Find the index of 1 in the array.
2. Initialize min_dist to infinity.
3. Iterate over the array from the index of 1:
   a. If the current element is 2, update min_dist to the distance between the current index and the index of 1.
4. Iterate over the array from the index of 1 to 0:
   a. If the current element is 2, update min_dist to the distance between the current index and the index of 1.
5. Return min_dist if it is not equal to infinity, otherwise return 0.
"""

def ClosestEnemy(arr):
    index_of_one = arr.index(1)
    min_dist = float('inf')
    for i in range(index_of_one, len(arr)):
        if arr[i] == 2:
            min_dist = min(min_dist, i - index_of_one)
            break
    for i in range(index_of_one, -1, -1):
        if arr[i] == 2:
            min_dist = min(min_dist, index_of_one - i)
            break
    return min_dist if min_dist != float('inf') else 0

                        # Two Pointer Method

# def ClosestEnemy(arr):
#     # find the index of the 1 in the array
#     index_of_one = arr.index(1)
    
#     # initialize left and right pointers
#     left = index_of_one - 1
#     right = index_of_one + 1
    
#     # initialize closest distance to a very large number
#     closest_distance = float('inf')
    
#     # iterate until the left or right pointer goes out of bounds
#     while left >= 0 or right < len(arr):
#         # if the left pointer is pointing to a 2, calculate the distance and update closest distance if necessary
#         if left >= 0 and arr[left] == 2:
#             distance = index_of_one - left
#             if distance < closest_distance:
#                 closest_distance = distance
        
#         # if the right pointer is pointing to a 2, calculate the distance and update closest distance if necessary
#         if right < len(arr) and arr[right] == 2:
#             distance = right - index_of_one
#             if distance < closest_distance:
#                 closest_distance = distance
        
#         # move the pointers to the next position
#         left -= 1
#         right += 1
    
#     # if no enemy was found, return 0
#     if closest_distance == float('inf'):
#         return 0
    
#     return closest_distance


"""
Both methods have a time complexity of O(n), where n is the 
length of the input array. However, in terms of space complexity, 
the two-pointer method is more efficient because it uses constant 
extra space, while the first method creates an additional list with 
a length equal to the number of enemies in the input array.
"""

print(ClosestEnemy([1, 0, 0, 0, 2, 2, 2])) # Output: 4
print(ClosestEnemy([2, 0, 0, 0, 2, 2, 1, 0])) # Output: 1
print(ClosestEnemy([0, 0, 0, 1, 0, 0, 0, 0])) # Output: 0
print(ClosestEnemy([1, 2, 0, 0, 2, 2, 2])) # Output: 1
print(ClosestEnemy([1, 0, 0, 2, 2, 2, 0])) # Output: 3

