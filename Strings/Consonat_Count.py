"""
Problem Statement                                            
  Have the function ConsonantCount(str) take the str string	
  parameter being passed and return the number of consonants 	
  the string contains.  					
                                                               
  Examples                                                     
  Input 1: "Hello World"                                       
  Output 1: 7		                                        
                                                               
  Input 2: "Alphabets"                                         
  Output 2: 6               
"""
"""
                                            Algorithm
1. Create an empty set named `vowels` which will store all vowels.

2. Create a variable named `count` and initialize it to zero.

3. Iterate through each character in the string:
   a. If the character is an alphabet and not in the set of vowels, 
   then increment the `count` variable.

4. Return the value of `count`.

"""


def ConsonantCount(strParam):
    vowels = set(['a', 'e', 'i', 'o', 'u'])
    count = 0
    for char in strParam:
        if char.isalpha() and char.lower() not in vowels:
            count += 1
    return count
 
# Test cases
input1 = "Hello World"
output1 = ConsonantCount(input1)
print("Input 1:", input1)
print("Output 1:", output1)

input2 = "Alphabets"
output2 = ConsonantCount(input2)
print("Input 2:", input2)
print("Output 2:", output2)

input3 = "Python Programming Language"
output3 = ConsonantCount(input3)
print("Input 3:", input3)
print("Output 3:", output3)

input4 = "Testing the Consonant Count function"
output4 = ConsonantCount(input4)
print("Input 4:", input4)
print("Output 4:", output4)

input5 = "aeiou"
output5 = ConsonantCount(input5)
print("Input 5:", input5)
print("Output 5:", output5)

input6 = "12345"
output6 = ConsonantCount(input6)
print("Input 6:", input6)
print("Output 6:", output6)
