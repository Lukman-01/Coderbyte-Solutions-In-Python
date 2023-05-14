"""
Problem Statement                                            
  Have the function EquivalentKeypresses(strArr) read the array
  of strings stored in strArr which will contain 2 strings     
  representing two comma separated lists of keypresses.        
  Your goal is to return the string true if the keypresses     
  produce the same printable string and the string false if    
  they do not.                                                 
                                                               
  A keypress can be either a printable character or a backspace
  represented by -B.                                           
                                                               
  You can produce a printable string from such a string of     
  keypresses by having backspaces erase one preceding character
                                                               
  For example: if strArr contains ["a,b,c,d", "a,b,c,c,-B,d"]  
  the output should return true because those keypresses       
  produce the same printable string.                           
                                                               
  The array given will not be empty. The keypresses will only  
  contain letters from the alphabet and backspaces.            
                                                               
  Examples                                                     
  Input 1: ["a,b,c,d", "a,b,c,d,-B,d"]	                        
  Output 1: true                                               
                                                               
  Input 2: ["c,a,r,d", "c,a,-B,r,d"]                           
  Output 2: false     
"""


# The data structure used in the `EquivalentKeypresses` function is a stack. 

# Here's the algorithm for the function:
# 1. Split the two strings in `strArr` by comma and store them in `string1` and `string2`.
# 2. Initialize two empty strings `s1` and `s2` to store the resulting strings after processing the keypresses.
# 3. Loop through each character in `string1`. If the character is a backspace (`-B`), skip it. 
#     Otherwise, check if the next character is also a backspace. If it is not, add the current 
#     character to `s1`. If it is, skip the current character and the next character (the backspace).
# 4. Repeat step 3 for `string2`.
# 5. If `s1` is equal to `s2`, return `True`. Otherwise, return `False`.

# The stack is used implicitly in the algorithm as we keep track of the characters 
# seen so far and remove them if we encounter a backspace.



def EquivalentKeypresses(strArr):
    s1, s2 = strArr
    stack1, stack2 = [], []
    
    for ch in s1.split(','):
        if ch == '-B':
            if stack1:
                stack1.pop()
        else:
            stack1.append(ch)

    for ch in s2.split(','):
        if ch == '-B':
            if stack2:
                stack2.pop()
        else:
            stack2.append(ch)

    return stack1 == stack2



# test cases
print(EquivalentKeypresses(["a,b,c,d", "a,b,c,d,-B,d"]))  # true
print(EquivalentKeypresses(["c,a,r,d", "c,a,-B,r,d"]))  # false
print(EquivalentKeypresses(["a,b,c,d", "a,b,-B,c,d"]))  # false
print(EquivalentKeypresses(["a,b,c,d", "a,b,d"]))  # false
print(EquivalentKeypresses(["a,b,c,d", "a,b,c,e,-B,d"]))  # true
