"""
Problem Statement                                            
  Have the function OffLineMinimum(strArr) take the strArr     
  parameter being passed which will be an array of integers    
  ranging from 1...n and the letter "E" and return the correct 
  subset based on the following rules. The input will be in    
  the following format: ["I","I","E","I",...,"E",...,"I"] where
  the I's stand for integers and the E means take out the      
  smallest integer currently in the whole set. When finished,  
  your program should return that new set with integers        
  separated by commas. For example: if strArr is               
  ["5","4","6","E","1","7","E","E","3","2"] then your program  
  should return 4,1,5.                                         
                                                               
  Examples                                                     
  Input 1: ["1","2","E","E","3"]                               
  Output 1: 1,2                                                
                                                               
  Input 2: ["4","E","1","E","2","E","3","E"]                   
  Output 2: 4,1,2,3            
"""

"""
Algorithm:
1. Create an empty list to store the result.
2. Create an empty list to act as a temporary stack.
3. Iterate through the given list:
     a. If the current element is an integer, append it to the temporary stack.
     b. If the current element is 'E', find the minimum element in the 
        temporary stack and append it to the result list. Then remove 
        that element from the temporary stack.
4. Return the result list as a string separated by commas.

Data Structure Used: Stack
"""



def OffLineMinimum(strArr):
    result = []
    stack = []
    for char in strArr:
        if char.isdigit():
            stack.append(int(char))
        elif char == 'E':
            min_num = min(stack)
            result.append(str(min_num))
            stack.remove(min_num)
    return ",".join(result)



print(OffLineMinimum(["1","2","E","E","3"])) # Output: "1,2"
print(OffLineMinimum(["4","E","1","E","2","E","3","E"])) # Output: "4,1,2,3"
print(OffLineMinimum(["5","4","6","E","1","7","E","E","3","2"])) # Output: "4,1,5"
print(OffLineMinimum(["1", "2", 'E', 'E', "3"]))  # "1,2"

 

