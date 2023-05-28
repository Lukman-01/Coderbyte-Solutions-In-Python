"""
Problem Statement                                            
  Have the function LetterCapitalize(str) take the str         
  parameter being passed and capitalize the first letter of    
  each word. Words will be separated by only one space.        
                                                               
  Examples                                                     
  Input 1: "hello world"                                       
  Output 1: Hello World                                        
                                                               
  Input 2: "i ran there"                                       
  Output 2: I Ran There  
"""



# Algorithm

# 1. Split the input string `strParam` into a list of words using the `split()` function.
# 2. Loop through each word in the list of words.
# 3. Capitalize the first letter of each word using the `capitalize()` function.
# 4. Join the list of words back together into a single string, separated by spaces.
# 5. Return the resulting string.


def LetterCapitalize(strParam):
    words = strParam.split()
    for i in range(len(words)):
        words[i] = words[i].capitalize()
    return " ".join(words)


# Test case 1: basic input
result1 = LetterCapitalize("hello world")
print(result1)  # Output should be "Hello World"

# Test case 2: input with all uppercase letters
result2 = LetterCapitalize("THIS IS ALL UPPERCASE")
print(result2)  # Output should be "This Is All Uppercase"

# Test case 3: input with numbers and special characters
result3 = LetterCapitalize("123 abc !@#")
print(result3)  # Output should be "123 Abc !@#"

# Test case 4: input with multiple spaces
result4 = LetterCapitalize("   hello   world   ")
print(result4)  # Output should be "Hello World"

# Test case 5: input with a coderbyte example letter
result5 = LetterCapitalize("i ran there")
print(result5)  # Output should be "I Ran There"
