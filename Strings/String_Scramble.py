"""
Problem Statement                                            
  Have the function StringScramble(str1,str2) take both         
  parameters being passed and return the string true if a      
  portion of str1 characters can be rearranged to match str2,  
  otherwise return the string false.                           
  For example: if str1 is "rkqodlw" and str2 is "world" the    
  output should return true. Punctuation and symbols will not  
  be entered with the parameters.                              
                                                               
  Examples                                                     
  Input 1: "cdore" & "coder"                                   
  Output 1: true                                               
                                                               
  Input 2: "h3llko" & "hello"                                  
  Output 2: false               
"""

def StringScramble(string1, string2):
    array1 = list(string1)
    array2 = list(string2)

    i = 0
    while i < len(array1):
        j = 0
        while j < len(array2):
            if array1[i] == array2[j]:
                array1.pop(i)
                array2.pop(j)
                i -= 1
                break
            j += 1
        i += 1

    if len(array2) == 0:
        return True
    else:
        return False

# Test cases
print(StringScramble("rkqodlw", "world"))   # Output: True
print(StringScramble("hello", "hey"))       # Output: False
print(StringScramble("abcde", "edcba"))     # Output: True


"""
Algorithm:

1. Convert `string1` and `string2` into lists of characters `array1` and `array2`, respectively.
2. Initialize a variable `i` to 0.
3. Iterate through the characters in `array1` using a while loop with the condition `i < len(array1)`:
   - Initialize a variable `j` to 0.
   - Iterate through the characters in `array2` using another while loop with the condition `j < len(array2)`:
      - If the character at `array1[i]` matches the character at `array2[j]`, remove both characters from `array1` and `array2`, and decrement `i` by 1 to account for the removal.
      - Break out of the inner loop once a match is found (to avoid unnecessary comparisons).
      - Increment `j` by 1 to check the next character in `array2`.
   - Increment `i` by 1 to check the next character in `array1`.
4. After the loops, check the length of `array2`:
   - If `array2` is empty (length is 0), it means all characters in `string2` were found in `string1`, and the function should return `True`.
   - Otherwise, return `False`.
"""