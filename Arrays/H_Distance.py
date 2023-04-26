"""
Problem Statement                                            
  Have the function HDistance(strArr) take the array of strings
  stored in strArr, which will only contain two strings of     
  equal length and return the number of characters at each     
  position that are different between them.                    
                                                               
  For example: if strArr is ["house", "hours"] then your       
  program should return 2. The string will always be of equal  
  length and will only contain lowercase characters from the   
  alphabet and numbers.                                        
                                                               
  Examples                                                     
  Input 1: ["10011", "10100"]                                  
  Output 1: 3                                                  
                                                               
  Input 2: ["abcdef", "defabc"]                                
  Output 2: 6            
"""
"""
                        Algorithm for HDistance(strArr):
1. Initialize a variable called count to zero.
2. Iterate over the characters in the first string of the array.
3. For each character, check if it is not equal to the corresponding character in the second string.
4. If the characters are different, increment the count.
5. Return the count.

"""
def HDistance(strArr):
    count = 0
    for i in range(len(strArr[0])):
        if strArr[0][i] != strArr[1][i]:
            count += 1
    return count
 

print(HDistance(["abcd", "abce"])) # Output: 1
print(HDistance(["12345", "67890"])) # Output: 5
print(HDistance(["same", "same"])) # Output: 0
print(HDistance(["xyzxyz", "xyzxyz"])) # Output: 0
print(HDistance(["abcde", "fghij"])) # Output: 5
