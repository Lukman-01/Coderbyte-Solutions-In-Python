"""
Problem Statement                                            
  Have the function HammingDistance(strArr) take the array of  
  strings stored in strArr, which will only contain two strings
  of equal length and return the Hamming distance between them.
  The Hamming distance is the number of positions where the    
  corresponding characters are different.                      
  For example: if strArr is ["coder", "codec"] then your       
  program should return 1. The string will always be of equal  
  length and will only contain lowercase characters from the   
  alphabet and numbers.                                        
                                                               
  Examples                                                     
  Input 1: ["10011", "10100"]                                  
  Output 1: 3                                                  
                                                               
  Input 2: ["helloworld", "worldhello"]                        
  Output 2: 8                     
"""

#  Algorithm:

# 1. Convert the two strings in the input array into character arrays.
# 2. Initialize a counter variable to 0.
# 3. Iterate through the character arrays:
#    a. If the character at the current position in the first array is different from the character at the corresponding position in the second array, increment the counter.
# 4. Return the counter as the Hamming distance.



def HammingDistance(strArr):
    return sum(ch1 != ch2 for ch1, ch2 in zip(strArr[0], strArr[1]))


print(HammingDistance(["10011", "10100"]))  # 3
print(HammingDistance(["helloworld", "worldhello"]))  # 8
print(HammingDistance(["abcdefg", "ABCDEFG"]))  # 7
print(HammingDistance(["abcd1234", "abdc2143"]))  # 6
