"""
Problem Statement                                            
  Have the function FizzBuzz(num) take the num parameter being 
  passed and return all the numbers from 1 to num separated by 
  spaces but replace every number that is divisible by 3       
  with the word "Fizz", replace every number that is divisible 
  by 5 with the word "Buzz", & every number that is divisible  
  by both 3 and 5 with the word "FizzBuzz".                    
  For example: if num is 16, the code should return the string 
  1 2 Fizz 4 Buzz Fizz 7 8 Fizz Buzz 11 Fizz 13 14 FizzBuzz 16 
  The input will be within the range 1 - 50.                   
                                                               
  Test Cases                                                   
  For example: if the input string is "Hello World and Coders" 
  then your program should return the string                   
  sredoC dna dlroW olleH.                                      
                                                               
  Examples                                                     
  Input 1: 3                                                   
  Output 1: "1 2 Fizz"                                         
                                                               
  Input 2: 8                                                   
  Output 2: "1 2 Fizz 4 Buzz Fizz 7 8" 
"""
"""
Algorithm:
1. Create an empty string variable called `result`.
2. Loop from 1 to num (inclusive).
3. If the current number is divisible by both 3 and 5, add "FizzBuzz" to `result`.
4. If the current number is divisible by 3, add "Fizz" to `result`.
5. If the current number is divisible by 5, add "Buzz" to `result`.
6. If the current number is not divisible by 3 or 5, add the current number to `result`.
7. Add a space after each number or word added to `result`.
8. Return `result` with trailing space removed.
"""

def FizzBuzz(num):
    result = ""
    for i in range(1, num+1):
        if i % 3 == 0 and i % 5 == 0:
            result += "FizzBuzz "
        elif i % 3 == 0:
            result += "Fizz "
        elif i % 5 == 0:
            result += "Buzz "
        else:
            result += str(i) + " "
    return result.strip()

print(FizzBuzz(3)) # "1 2 Fizz"
print(FizzBuzz(8)) # "1 2 Fizz 4 Buzz Fizz 7 8"
print(FizzBuzz(15)) # "1 2 Fizz 4 Buzz Fizz 7 8 Fizz Buzz 11 Fizz 13 14 FizzBuzz"
