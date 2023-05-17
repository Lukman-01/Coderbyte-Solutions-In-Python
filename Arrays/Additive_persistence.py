"""
 Problem Statement                                            
  Have the function AdditivePersistence(num) take the num      
  parameter being passed which will always be a positive       
  integer and return its additive persistence which is the     
  number of times you must add the digits in num until you     
  reach a single digit. For example: if num is 2718 then your  
  program should return 2                                      
  because 2 + 7 + 1 + 8 = 18 and 1 + 8 = 9 and you stop at 9.  
                                                               
  Examples                                                     
  Input 1: 4                                                   
  Output 1: 0                                                  
                                                               
  Input 2: 19                                                  
  Output 2: 2       
"""

# Algorithm:
# 1. Define a variable 'count' and initialize it to zero.
# 2. Check if the given number 'num' is a single digit or not. If yes, return count.
# 3. Otherwise, convert the number 'num' into a string and loop through its digits.
# 4. Add the digits and store the sum in a variable 'total'.
# 5. Increment the count by 1.
# 6. Recursively call the AdditivePersistence function with the 'total' as the new input.
# 7. Return the result obtained from the recursive call.

def AdditivePersistence(num):
    count = 0
    while num >= 10:
        total = 0
        for digit in str(num):
            total += int(digit)
        num = total
        count += 1
    return count


print(AdditivePersistence(4))   # Output: 0
print(AdditivePersistence(19))  # Output: 2
print(AdditivePersistence(2718)) # Output: 2
print(AdditivePersistence(12345)) # Output: 2
print(AdditivePersistence(888)) # Output: 2
