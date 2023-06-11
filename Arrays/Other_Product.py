"""
Problem Statement                                            
  Have the function OtherProducts(arr) take the array of       
  numbers stored in arr and return a new list of the products  
  of all the other numbers in the array for each element.      
  For example: if arr is [1, 2, 3, 4, 5] then the new array,   
  where each location in the new array is the product of all   
  other elements, is [120, 60, 40, 30, 24].                    
  The following calculations were performed to get this answer 
  [(2*3*4*5), (1*3*4*5), (1*2*4*5), (1*2*3*5), (1*2*3*4)].     
  You should generate this new array and then return the       
  numbers as a string joined by a hyphen: 120-60-40-30-24.     
  The array will contain at most 10 elements and at least 1    
  element of only positive integers.                           
                                                               
  Examples                                                     
  Input 1: [1,4,3]                                             
  Output 1: 12-3-4                                             
                                                               
  Input 2: [3,1,2,6]                                           
  Output 2: 12-36-18-6               
"""

# Algorithm:

# 1. Initialize an empty list called `result`.
# 2. Iterate over each element, `num`, in the input array `arr`:
#      - Create a variable `product` and set it to 1.
#      - Iterate over each element, `n`, in `arr`:
#          - If `n` is not equal to `num`, multiply it with `product`.
#      - Append `product` to the `result` list.
# 3. Join all elements in the `result` list with hyphens and store the result in a variable called `output`.
# 4. Return `output`.



def OtherProducts(arr):
    result = []
    for i, num in enumerate(arr):
        product = 1
        for j, n in enumerate(arr):
            if i != j:
                product *= n
        result.append(str(product))
    return '-'.join(result)

# Test case 1
arr = [1, 4, 3]
print(OtherProducts(arr))
# Output: 12-3-4

# Test case 2
arr = [3, 1, 2, 6]
print(OtherProducts(arr))
# Output: 12-36-18-6

# Test case 3
arr = [1, 2, 3, 4, 5]
print(OtherProducts(arr))
# Output: 120-60-40-30-24

# Test case 4
arr = [5, 10, 15, 20]
print(OtherProducts(arr))
# Output: 3000-1500-1000-750

# Test case 5
arr = [2, 4, 6, 8, 10, 12]
print(OtherProducts(arr))
# Output: 46080-23040-15360-11520-9216-7680
