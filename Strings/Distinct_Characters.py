"""
roblem Statement                                            
  Have the function DistinctCharacters(str) take the str       
  parameter being passed and determine if it contains at least 
  10 distinct characters, if so, then your program should      
  return the string true, otherwise it should return the string
  false. For example: if str is "abc123kkmmmm?" then your      
  program should return the string false because this string   
  contains only                                                
  9 distinct characters: a, b, c, 1, 2, 3, k, m, ? adds up to 9
                                                               
  Examples                                                     
  Input 1: 12334bbmma:=6                                       
  Output 1: true                                               
                                                               
  Input 2: eeeemmmmmmmmm1000                                   
  Output 2: false              
"""

                                        #Algorithm
                                        
def DistinctCharacters(str):
    # create a set of the characters in the string
    chars = set(str)
    # check if the set has at least 10 elements
    if len(chars) >= 10:
        return "true"
    else:
        return "false"



print(DistinctCharacters("12334bbmma:=6")) # true
print(DistinctCharacters("eeeemmmmmmmmm1000")) # false

