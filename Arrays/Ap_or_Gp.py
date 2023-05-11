"""
Problem Statement                                            
  Have the function ArithGeo(arr) take the array of numbers    
  stored in arr and return the string "Arithmetic" if the      
  sequence follows an arithmetic pattern or return "Geometric" 
  if it follows a geometric pattern. If the sequence doesn't   
  follow either pattern return -1. An arithmetic sequence is   
  one where the difference between each of the numbers is      
  consistent, where as in a geometric sequence, each term after
  the first is multiplied by some constant or common ratio.    
  Arithmetic example: [2, 4, 6, 8] and                         
  Geometric example: [2, 6, 18, 54]. Negative numbers may be   
  entered as parameters, 0 will not be entered, and no array   
  will contain all the same elements.                          
                                                               
  Examples                                                     
  Input 1: new int[] {5,10,15}                                 
  Output 1: Arithmetic                                         
                                                               
  Input 2: new int[] {2,4,16,24}                               
  Output 2: -1                         
"""

"""
Algorithm:
1. Find the difference between the second and the first element of the array
2. Check if the difference is the same between each element in the array. If it is, then it follows an arithmetic pattern.
3. If the difference is not the same between each element, find the ratio between the second and the first element of the array.
4. Check if the ratio is the same between each element in the array. If it is, then it follows a geometric pattern.
5. If both steps 2 and 4 fail, then return -1.
"""
 
def ArithGeo(arr):
    diff = arr[1] - arr[0]
    ratio = arr[1] / arr[0]
    
    is_arithmetic = True
    is_geometric = True
    
    for i in range(2, len(arr)):
        if arr[i] - arr[i-1] != diff:
            is_arithmetic = False
        if arr[i] / arr[i-1] != ratio:
            is_geometric = False
        
        # optimization: if both is_arithmetic and is_geometric are False, we can return -1
        if not is_arithmetic and not is_geometric:
            return -1
        
    if is_arithmetic:
        return "Arithmetic"
    elif is_geometric:
        return "Geometric"
    else:
        return -1
 
        
# Test Case 1
print(ArithGeo([2, 6, 18, 54]))

# Test Case 2
print(ArithGeo([2, 4, 16, 24]))

# Test Case 3
print(ArithGeo([1, 2, 3, 4, 5]))

# Test Case 4
print(ArithGeo([2, 4, 8, 16, 32]))

# Test Case 5
print(ArithGeo([5, 7, 9, 11]))
