"""
Problem Statement                                            
  Have the function VowelCount(str) take the str string        
  parameter being passed and return the number of vowels the   
  string contains (ie. "All cows eat grass and moo" would      
  return 8). Do not count y as a vowel for this challenge.     
                                                               
  Examples                                                     
  Input 1: "hello"                                             
  Output 1: 2                                                  
                                                               
  Input 2: "coderbyte"                                         
  Output 2: 3     
"""

def VowelCount(str):
    vowels = "aeiouAEIOU" # Define the list of vowels
    count = 0 # Initialize count to 0

    # Iterate through each character in the input string
    for char in str:
        if char in vowels: # If the character is a vowel
            count += 1 # Increment count by 1

    return count # Return the total count of vowels in the string

print(VowelCount("hello")) # Output: 2
print(VowelCount("coderbyte")) # Output: 3
print(VowelCount("Lukman")) # Output: 2
