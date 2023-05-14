"""
Problem Statement                                            
  Have the function MatrixSpiral(strArr) read the array of     
  strings stored in strArr which will represent a 2D N matrix, 
  and your program should return the elements after printing   
  them in a clockwise, spiral order. You should return the     
  newly formed list of elements as a string with the numbers   
  separated by commas.                                         
                                                               
  For example: strArr is "[1, 2, 3]", "[4, 5, 6]", "[7, 8, 9]" 
  then this looks like the following 2D matrix:                
                               1 2 3                           
                               4 5 6                           
                               7 8 9                           
  So your program should return the elements of this matrix in 
  a clockwise, spiral order which is: 1,2,3,6,9,8,7,4,5        
                                                               
  Examples                                                     
  Input 1: ["[1, 2]", "[10, 14]"]                              
  Output 1: 1,2,14,10                                          
                                                               
  Input 2: ["[4, 5, 6, 5]", "[1, 1, 2, 2]", "[5, 4, 2, 9]"]    
  Output 2: 4,5,6,5,2,9,2,4,5,1,1,2    
"""
"""
Algorithm:
1. Initialize 4 variables, top, bottom, left, right with values 0, rows-1, 0, cols-1 respectively
2. Initialize an empty list, spiral, to store the spiral order of elements
3. Run a loop until top<=bottom and left<=right
   a. Loop through the first row (top) from left to right, 
    add each element to spiral list and increment top by 1
   b. Loop through the last column (right) from top to bottom, 
    add each element to spiral list and decrement right by 1
   c. If top<=bottom and left<=right, loop through the last row (bottom) 
    from right to left, add each element to spiral list and decrement bottom by 1
   d. If top<=bottom and left<=right, loop through the first 
    column (left) from bottom to top, add each element to spiral list and increment left by 1
4. Join the elements in the spiral list with comma separator and return as a string

Time Complexity: O(rows x cols)
Space Complexity: O(rows x cols)
"""

def MatrixSpiral(strArr):
    matrix = []
    for row in strArr:
        matrix.append(eval(row))  # convert string representation of list to list
        #Using eval() allows the code to convert each string representation of a list into an actual Python list, 
        # so that it can be processed and manipulated as a matrix in the subsequent code. 
    rows, cols = len(matrix), len(matrix[0])
    top, bottom, left, right = 0, rows-1, 0, cols-1
    spiral = []
    while top <= bottom and left <= right:
        # traverse the first row from left to right
        for i in range(left, right+1):
            spiral.append(matrix[top][i])
        top += 1
        
        # traverse the last column from top to bottom
        for i in range(top, bottom+1):
            spiral.append(matrix[i][right])
        right -= 1
        
        # traverse the last row from right to left
        if top <= bottom:
            for i in range(right, left-1, -1):
                spiral.append(matrix[bottom][i])
            bottom -= 1
        
        # traverse the first column from bottom to top
        if left <= right:
            for i in range(bottom, top-1, -1):
                spiral.append(matrix[i][left])
            left += 1
    
    return ','.join(map(str, spiral))



print(MatrixSpiral(["[1, 2]", "[10, 14]"]))
    #Output: "1,2,14,10"
print(MatrixSpiral(["[1, 2, 3]", "[4, 5, 6]", "[7, 8, 9]"]))
    #Output: "1,2,3,6,9,8,7,4,5"
print(MatrixSpiral(["[1, 2, 3, 4]", "[5, 6, 7, 8]", "[9, 10, 11, 12]", "[13, 14, 15, 16]"])) 
    #Output: "1,2,3,4,8,12,16,15,14,13,9,5,6,7,11,10"
print(MatrixSpiral(["[1, 2, 3, 4, 5]", "[6, 7, 8, 9, 10]", "[11, 12, 13, 14, 15]", "[16, 17, 18, 19, 20]", "[21, 22, 23, 24, 25]"])) 
    #Output: "1,2,3,4,5,10,15,20,25,24,23,22,21,16,11,6,7,8,9,14,19,18,17,12,13"
print(MatrixSpiral(["[1, 2, 3, 4, 5]", "[6, 7, 8, 9, 10]", "[11, 12, 13, 14, 15]", "[16, 17, 18, 19, 20]"]))
    #Output: "1,2,3,4,5,10,15,20,19,18,17,16,11,6,7,8,9,14,13,12"