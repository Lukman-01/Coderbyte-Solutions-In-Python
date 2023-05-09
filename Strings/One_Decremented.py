"""
Problem Statement                                            
  Have the function OneDecremented(str) count how many times a 
  digit appears that is exactly one less than the previous     
  digit. For example: if str is "5655984" then your program    
  should return 2 because 5 appears directly after 6 and 8     
  appears directly after 9. The input will always contain at   
  least 1 digit.	                                        
                                                               
  Examples                                                     
  Input 1: "56"                                                
  Output 1: 0                                                  
                                                               
  Input 2: "9876541110"                                        
  Output 2: 6           
"""
"""
                Algorithm
1. Initialize a counter variable to 0.
2. Loop through each digit in the string, starting from the second digit.
3. Compare the current digit with the previous digit.
4. If the current digit is exactly one less than the previous digit, increment the counter.
5. After looping through the entire string, return the counter.
"""


def OneDecremented(str):
    count = 0
    for i in range(1, len(str)):
        if int(str[i]) == int(str[i-1])-1:
            count += 1
    return count

print(OneDecremented("56")) # Output: 0
print(OneDecremented("9876541110")) # Output: 6
print(OneDecremented("44433")) # Output: 1
print(OneDecremented("132")) # Output: 1
print(OneDecremented("01234")) # Output: 0
