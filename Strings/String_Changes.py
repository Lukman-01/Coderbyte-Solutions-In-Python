"""
Problem Statement                                            
  Have the function StringChanges(str) take the str parameter  
  being passed, which will be a string containing letters from 
  the alphabet, and return a new string based on the following 
  rules. Whenever a capital M is encountered, duplicate the    
  previous character (then remove the M), and whenever a       
  capital N is encountered remove the next character from the  
  string (then remove the N). All other characters in the      
  string will be lowercase letters.                            
  For example: "abcNdgM" should return "abcgg".                
  The final string will never be empty.                          
                                                               
  Examples                                                     
  Input 1: "MrtyNNgMM"                                         
  Output 1: rtyggg                                             
                                                               
  Input 2: "oMoMkkNrrN"                                        
  Output 2: ooookkr
"""
"""
Algorithm:
1. Initialize an empty string called result.
2. Traverse through each character in the string.
3. If the current character is "M", then append the previous character twice to the result.
4. If the current character is "N", then skip the next character.
5. If the current character is not "M" or "N", then simply append it to the result.
6. Return the result string.

"""


def StringChanges(str):
    result = ""
    n = len(str)
    i = 0
    while i < n:
        if str[i] == "M":
            if i > 0:
                result += str[i-1] * 2
            i += 1
        elif str[i] == "N":
            i += 2
        else:
            result += str[i]
            i += 1
    return result




# Test case 1
input1 = "MrtyNNgMM"
output1 = StringChanges(input1)
print(output1)  # Expected output: rtyggg

# Test case 2
input2 = "oMoMkkNrrN"
output2 = StringChanges(input2)
print(output2)  # Expected output: ooookkr

# Test case 3
input3 = "abcNdgM"
output3 = StringChanges(input3)
print(output3)  # Expected output: abcgg
