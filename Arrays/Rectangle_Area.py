"""
Problem Statement                                            
  Have the function RectangleArea(strArr) take the array of    
  strings stored in strArr, which will only contain 4 elements 
  and be in the form (x y) where x and y are both integers, and
  return the area of the rectangle formed by the 4 points on a 
  Cartesian grid. The 4 elements will be in arbitrary order.   
  For example: strArr is ["(0 0)", "(3 0)", "(0 2)", "(3 2)"]  
  then your program should return 6 because the width of the   
  rectangle is 3 and the height is 2 and the area of a         
  rectangle is equal to the width * height.                    
                                                               
  Examples                                                     
  Input 1: ["(1 1)","(1 3)","(3 1)","(3 3)"]                   
  Output 1: 4                                                  
                                                               
  Input 2: ["(0 0)","(1 0)","(1 1)","(0 1)"]                   
  Output 2: 1   
"""

"""
1. Initialize four variables: `min_x`, `max_x`, `min_y`, and `max_y` to the first point's x and y coordinates.
2. Loop through the remaining three points:
   a. Update `min_x` and `max_x` if necessary.
   b. Update `min_y` and `max_y` if necessary.
3. Calculate the width of the rectangle as `max_x - min_x`.
4. Calculate the height of the rectangle as `max_y - min_y`.
5. Calculate the area of the rectangle as `width * height`.
6. Return the area as the output.
"""
 

def RectangleArea(strArr):
    # Step 1
    x1, y1 = map(int, strArr[0].strip('()').split())
    min_x = max_x = x1
    min_y = max_y = y1

    # Step 2
    for point in strArr[1:]:
        x, y = map(int, point.strip('()').split())
        if x < min_x:
            min_x = x
        elif x > max_x:
            max_x = x
        if y < min_y:
            min_y = y
        elif y > max_y:
            max_y = y

    # Step 3
    width = max_x - min_x

    # Step 4
    height = max_y - min_y

    # Step 5
    area = width * height

    # Step 6
    return area
 
# Test Case 1
arr1 = ["(1 1)","(1 3)","(3 1)","(3 3)"]
print(RectangleArea(arr1)) # Output: 4

# Test Case 2
arr2 = ["(0 0)","(1 0)","(1 1)","(0 1)"]
print(RectangleArea(arr2)) # Output: 1

# Test Case 3
arr3 = ["(0 0)","(3 0)","(0 2)","(3 2)"]
print(RectangleArea(arr3)) # Output: 6

# Test Case 4
arr4 = ["(0 0)","(5 0)","(0 3)","(5 3)"]
print(RectangleArea(arr4)) # Output: 15

# Test Case 5
arr5 = ["(1 1)","(4 1)","(4 4)","(1 4)"]
print(RectangleArea(arr5)) # Output: 9

