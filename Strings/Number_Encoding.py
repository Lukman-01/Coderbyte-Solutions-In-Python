"""
Problem Statement                                            
  Have the function NumberEncoding(str) take the str parameter 
  and encode the message according to the following rule:      
  encode every letter into its corresponding numbered position 
  in the alphabet. Symbols and spaces will also be used in the 
  input. For example: if str is "af5c a#!" then your program   
  should return 1653 1#!.                                      
                                                               
  Examples                                                     
  Input 1: "hello 45"                                          
  Output 1: 85121215 45                                        
                                                               
  Input 2: "jaj-a"                                             
  Output 2: 10110-1                    
"""
"""
Algorithm:
1. Create an empty result string to hold the encoded message.
2. For each character in the input string:
   a. If the character is an alphabet, get its corresponding number 
        position in the alphabet using the ord() function.
   b. If the character is not an alphabet, simply add it to the result string as is.
3. Return the encoded message.
"""
def NumberEncoding(strparam):
    # Define a dictionary to map each letter to its corresponding position in the alphabet
    alphabet = {chr(i + ord('a')): str(i + 1) for i in range(26)}
    
    # Initialize an empty string to store the encoded message
    encoded = ""
    
    # Loop over each character in the input string
    for char in strparam:
        if char.isalpha():
            # If the character is a letter, add its corresponding number to the encoded string
            encoded += alphabet[char.lower()]
        else:
            # If the character is not a letter, add it to the encoded string as-is
            encoded += char
    
    return encoded
    

print(NumberEncoding("hello 45"))  # Output: 85121215 45
print(NumberEncoding("jaj-a"))     # Output: 10110-1
print(NumberEncoding("af5c a#!"))  # Output: 1653 1#!
print(NumberEncoding("z"))         # Output: 26
print(NumberEncoding(""))          # Output: ""

 