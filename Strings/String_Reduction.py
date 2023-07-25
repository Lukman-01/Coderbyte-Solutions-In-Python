"""
Problem Statement                                            
  Have the function StringReduction(str) take the str parameter
  being passed and return the smallest number you can get      
  through the following reduction method.                      
  The method is: Only the letters a, b, and c will be given in 
  str and you must take two different adjacent characters and  
  replace it with the third. For example "ac" can be replaced  
  with "b" but "aa" cannot be replaced with anything.          
  This method is done repeatedly until the string cannot be    
  further reduced, and the length of the resulting string is   
  to be outputted.                                             
                                                               
  For example: if str is "cab", "ca" can be reduced to "b"     
  and you get "bb" (you can also reduce it to "cc").           
  The reduction is done so the output should be 2.             
                                                               
  If str is "bcab", "bc" reduces to "a", so you have "aab",    
  then "ab" reduces to "c", and the final string "ac" is       
  reduced to "b" so the output should be 1.                    
                                                               
  Examples                                                     
  Input 1: "abcabc"                                            
  Output 1: 2                                                  
                                                               
  Input 2: cccc                                                
  Output 2: 4     
"""

def StringReduction(string):
    string_reductions = {
        "ab": "c",
        "ac": "b",
        "bc": "a",
        "ca": "b",
        "cb": "a"
    }
    string_reduction = ""
    flag = False
    i = 0

    while i < len(string):
        if i < len(string) - 1:
            substring = string[i] + string[i+1]
            if substring in string_reductions:
                flag = True
                string_reduction += string_reductions[substring]
                i += 2
            else:
                string_reduction += string[i]
                i += 1
        else:
            string_reduction += string[i]
            i += 1

    if flag:
        return StringReduction(string_reduction)
    else:
        return len(string_reduction)

# Test cases
print(StringReduction("cab"))  # Output: 2
print(StringReduction("bcab")) # Output: 1
print(StringReduction("ccccc")) # Output: 5

"""
Algorithm:

1. Create a dictionary `string_reductions` that maps the pairs "ab", "ac", "bc", "ca", and "cb" to their corresponding reduced characters "c", "b", "a", "b", and "a".
2. Initialize an empty string `string_reduction`.
3. Initialize a boolean variable `flag` to False. This flag will be used to determine if any replacements were made during the current iteration.
4. Initialize a variable `i` to 0.
5. Iterate through the characters of the input `string` using a while loop:
   - If `i` is less than the length of the string minus 1, check if the current character and the next character (substring of length 2) exist in `string_reductions`.
   - If a replacement is found, set the `flag` to True, append the replacement character to `string_reduction`, and increment `i` by 2 to skip the next character.
   - If no replacement is found, append the current character to `string_reduction`, and increment `i` by 1.
   - Repeat until all characters of the input string are processed.
6. After the loop, check the value of the `flag`:
   - If `flag` is True, it means replacements were made during this iteration, so recursively call the `StringReduction` function with the `string_reduction` as the new input.
   - If `flag` is False, it means no replacements were made during this iteration, so return the length of the `string_reduction` as the result.
7. The function returns the final reduced length.
"""