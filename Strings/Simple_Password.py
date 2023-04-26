"""
Problem Statement                                            
  Have the function SimplePassword(str) take the str parameter 
  being passed and determine if it passes as a valid password  
  that follows the list of constraints:                        
  1. It must have a capital letter.                            
  2. It must contain at least one number.                      
  3. It must contain a punctuation mark.                       
  4. It cannot have the word "password" in the string.         
  5. It must be longer than 7 characters and                    
     shorter than 31 characters.                               
  If all the above constraints are met within the string, the  
  your program should return the string true, otherwise your   
  program should return the string false.                      
  For example: if str is "apple!M7" then your program should   
  return "true".                                               
                                                               
  Examples                                                     
  Input 1: "passWord123!!!!"                                   
  Output 1: false                                              
                                                               
  Input 2: "turkey90AAA="                                      
  Output 2: true     
"""

def SimplePassword(str):
    # Check if the string meets all the constraints
    if any(c.isupper() for c in str) and \
       any(c.isdigit() for c in str) and \
       any(c in "!@#$%^&*()-+?_=,<>/\|{}[]~" for c in str) and \
       "password" not in str.lower() and \
       7 < len(str) < 31:
           return "true"
    else:
        return "false"

# This if statement checks if any of the given password requirements 
# are not met in the input string str. It starts by checking if the 
# string has a capital letter using the any() function that 
# returns True if any of the characters in the string meet the 
# given condition. If there is no uppercase character, it immediately returns false.

# Next, it checks if there is at least one digit in the string 
# using the same any() function, and returns false if it is not found.

# Then, it checks if the string contains at least one punctuation 
# mark from the string.punctuation list. If there is no punctuation mark, it returns false.

# Afterwards, it checks if the string length is greater than 7 and 
# less than 31. If the length is less than or equal to 7 or greater than or equal to 31, it returns false.

# Finally, it checks if the lowercase string of the input string contains 
# the substring "password". If the substring is found, it returns false.


# If all the password requirements are met, it returns true.

print(SimplePassword("passWord123!!!!"))  # false
print(SimplePassword("turkey90AAA="))     # true
print(SimplePassword("Abcdefg1!"))        # false
print(SimplePassword("noPunctuations"))   # false
print(SimplePassword("p4ssw0rd"))         # false
print(SimplePassword("VeryLongPasswordThatIsMoreThanThirtyCharacters"))  # false
print(SimplePassword("ValidP@ssw0rd"))    # true