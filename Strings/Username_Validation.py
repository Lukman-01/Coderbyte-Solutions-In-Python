"""
Problem Statement                                            
  Have the function CodelandUsernameValidation(str) take the   
  str parameter being passed and determine if the string is a  
  valid username according to the following rules:             
  1. The username is between 4 and 25 characters.              
  2. It must start with a letter.                              
  3. It can only contain letters, numbers, & underscore.       
  4. It cannot end with an underscore character.               
  If the username is valid then your program should return the 
  string true, otherwise return the string false.              
                                                               
  Examples                                                     
  Input 1: "aa_"                                               
  Output 1: false                                              
                                                               
  Input 2: "u__hello_world123"                                 
  Output 2: true        
"""

"""
                                    Algorithm

To solve this problem, we need to check if the given string satisfies all the rules for a valid username. Here's an algorithm that we can use:

1. Check if the length of the string is between 4 and 25 characters.
2. Check if the first character is a letter.
3. Check if the string contains only letters, numbers, and underscores.
4. Check if the last character is not an underscore.

"""

def CodelandUsernameValidation(str):
    if len(str) < 4 or len(str) > 25:
        return "false"
    if not str[0].isalpha():
        return "false"
    for c in str:
        if not (c.isalpha() or c.isdigit() or c == "_"):
            return "false"
    if str[-1] == "_":
        return "false"
    return "true"
 


def test_CodelandUsernameValidation():
    assert CodelandUsernameValidation("aa_") == "false"
    assert CodelandUsernameValidation("u__hello_world123") == "true"
    assert CodelandUsernameValidation("hello") == "true"
    assert CodelandUsernameValidation("1234") == "false"
    assert CodelandUsernameValidation("username_is_too_long_to_be_valid") == "false"
    print("All test cases pass")

test_CodelandUsernameValidation()

 

