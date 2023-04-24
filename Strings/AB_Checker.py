"""
Problem Statement                                            
  Have the function ABCheck(str) take the str parameter being  
  passed and return the string true if the characters a and b  
  are separated by exactly 3 places anywhere in the string at  
  least once (ie. "lane borrowed" would result in true because 
  there is exactly three characters between a and b).          
  Otherwise return the string false.                           
                                                               
  Examples                                                     
  Input 1: after badly                                         
  Output 1: false                                              
                                                               
  Input 2: Laura sobs                                          
  Output 2: true              
 """

""" 
                                Algorithm
To solve the problem, you can follow these steps:

1. Convert the input string to lowercase to make it case-insensitive.

2. Iterate through each character in the string and check if the current character is 'a'.

3. If the current character is 'a', check if there are exactly three characters after it, followed by the character 'b'.

4. If step 3 is true, return 'true' since the condition is met.

5. If there are no more characters to check and the condition is not met, return 'false'.

"""
#Here's the implementation in Python:


def ABCheck(str):
    str = str.lower()
    for i in range(len(str)):
        if str[i] == 'a' and i + 4 < len(str) and str[i+4] == 'b':
            return 'true'
    return 'false'

# Example 1: Check if "abcdef" contains 'a' and 'b' separated by 3 characters
result1 = ABCheck("abcdef")
print(result1)    # Output: false

# Example 2: Check if "aabccbb" contains 'a' and 'b' separated by 3 characters
result2 = ABCheck("aabccbb")
print(result2)    # Output: true

# Example 3: Check if "aBcDb" contains 'a' and 'b' separated by 3 characters
result3 = ABCheck("aBcDb")
print(result3)    # Output: true

# Example 4: Check if "a" contains 'a' and 'b' separated by 3 characters
result4 = ABCheck("a")
print(result4)    # Output: false

result5 = ABCheck("after badly")
print(result5)      # Output: false

result6 = ABCheck("Laura sobs")
print(result6)      # Output: true
