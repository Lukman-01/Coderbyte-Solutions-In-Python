"""
Problem Statement                                            
  Have the function TimeConvert(num) take the num parameter    
  being passed and return the number of hours and minutes the  
  parameter converts to (ie. if num = 63 then the output       
  should be 1:3). Separate the number of hours and minutes     
  with a colon.                                                
                                                               
  Examples                                                     
  Input 1: 126                                                 
  Output 1: 2:6                                                
                                                               
  Input 2: 45                                                  
  Output 2: 0:45              
"""

def TimeConvert(num):
    hours = num // 60
    minutes = num % 60
    return str(hours) + ":" + str(minutes)

# Test cases
print(TimeConvert(123))   # Output: "2:3"
print(TimeConvert(60))    # Output: "1:0"
print(TimeConvert(3600))  # Output: "60:0"
print(TimeConvert(126))   # Output: "2:6"
print(TimeConvert(45))   # Output: "0:45"
