"""
Problem Statement                                            
  Have the function ScaleBalancing(strArr) read strArr which   
  will contain two elements, the first being the two positive  
  integer weights on a balance scale (left and right sides)    
  and the second element being a list of available weights as  
  positive integers. Your goal is to determine if you can      
  balance the scale by using the least amount of weights from  
  the list, but using at most only 2 weights.                  
                                                               
  For example: if strArr is ["[5, 9]", "[1, 2, 6, 7]"] then    
  this means there is a balance scale with a weight of 5 on    
  the left side and 9 on the right side. It is in fact         
  possible to balance this scale by adding a 6 to the left     
  side from the list of weights and adding a 2 to the right    
  side. Both scales will now equal 11 and they are perfectly   
  balanced.                                                    
                                                               
  Your program should return a comma separated string of the   
  weights that were used from the list in ascending order,     
  so for this example your code should return the string 2,6   
                                                               
  There will only ever be one unique solution and the list of  
  available weights will not be empty. It is also possible to  
  add two weights to only one side of the scale to balance it. 
  If it is not possible to balance the scale then your program 
  should return the string not possible.                       
                                                               
  Examples                                                     
  Input 1: ["[3, 4]", "[1, 2, 7, 7]"]                          
  Output 1: 1                                                  
                                                               
  Input 2: ["[13, 4]", "[1, 2, 3, 6, 14]"]                     
  Output 2: 3,6                                       
"""

# Algorithm

# 1. Extract the left and right weights from the first element of `strArr`.
#    - Remove the square brackets and split the string by the comma.
#    - Convert the two resulting strings to integers and assign them to variables `left_weight` and `right_weight`.

# 2. Extract the list of available weights from the second element of `strArr`.
#    - Remove the square brackets and split the string by the comma.
#    - Convert each resulting string to an integer and store them in a list named `available_weights`.

# 3. Check if the left and right weights are already balanced.
#    - If `left_weight` is equal to `right_weight`, return an empty string.

# 4. Iterate over the available weights:
#    - For each weight `w1` in `available_weights`, check if `left_weight + w1` or `right_weight + w1` equals the opposite side weight.
#    - If a match is found, return the string representation of `w1`.

# 5. If no match is found, iterate over pairs of available weights:
#    - For each pair of weights (`w1`, `w2`) in `available_weights`, check if `left_weight + w1 + w2` or `right_weight + w1 + w2` equals the opposite side weight.
#    - If a match is found, return the string representation of `w1` and `w2`, separated by a comma.

# 6. If no match is found after checking all available weights, return the string "not possible".

 
def ScaleBalancing(strArr):
    left_weight, right_weight = map(int, strArr[0][1:-1].split(', '))
    available_weights = list(map(int, strArr[1][1:-1].split(', ')))

    if left_weight == right_weight:
        return ""

    for w1 in available_weights:
        if left_weight + w1 == right_weight or right_weight + w1 == left_weight:
            return str(w1)

    for i in range(len(available_weights)):
        for j in range(i + 1, len(available_weights)):
            w1 = available_weights[i]
            w2 = available_weights[j]
            if left_weight + w1 + w2 == right_weight or right_weight + w1 + w2 == left_weight:
                return str(w1) + "," + str(w2)

    return "not possible"
 

# Test case 1: Add weights 1 to the left side and balance the scale
print(ScaleBalancing(["[3, 4]", "[1, 2, 7, 7]"]))  # Output: 1

# Test case 2: Add weights 3 and 6 to the right side and balance the scale
print(ScaleBalancing(["[13, 4]", "[1, 2, 3, 6, 14]"]))  # Output: 3,6

# Test case 3: The scale is already balanced
print(ScaleBalancing(["[2, 2]", "[1, 2, 3, 4]"]))  # Output: ""

# Test case 4: Add weights 1 and 3 to the left side and balance the scale
print(ScaleBalancing(["[8, 6]", "[1, 3, 5, 7, 9]"]))  # Output: not possible

# Test case 5: It is not possible to balance the scale
print(ScaleBalancing(["[4, 10]", "[1, 2, 3, 5, 7]"]))  # Output: 1,5
