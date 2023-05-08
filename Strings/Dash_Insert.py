"""
Problem Statement                                            
  Have the function DashInsert(str) insert dashes ('-')        
  between each two odd numbers in str. For example: if str is  
  454793 the output should be 4547-9-3. Don't count zero as an 
  odd number.                                                  
                                                               
  Examples                                                     
  Input 1: 99946                                               
  Output 1: 9-9-946                                            
                                                               
  Input 2: 56730                                               
  Output 2: 567-30        
"""

"""
                                    Algorithm

Here's the outline of the algorithm for the `DashInsert` function:

1. Convert the input number `str` to a string.
2. Initialize an empty string `result`.
3. Iterate over the string, checking each pair of adjacent digits:
   a. If both digits are odd, add a dash '-' to `result` followed by the second digit.
   b. Otherwise, add the second digit to `result` without a dash.
4. Return the resulting string `result`.
"""
 

def DashInsert(Str):
    # convert str to a string
    Str = str(Str)
    # initialize an empty string for the result
    result = ""
    # iterate over the string, checking adjacent digits
    for i in range(len(Str)-1):
        # check if both digits are odd
        if int(Str[i]) % 2 == 1 and int(Str[i+1]) % 2 == 1:
            result += Str[i] + "-"
        else:
            result += Str[i]
    # add the last digit to the result
    result += Str[-1]
    return result

    
def test_DashInsert():
    assert DashInsert(99946) == "9-9-946"
    assert DashInsert(56730) == "567-30"
    assert DashInsert(13579) == "1-3-5-7-9"
    assert DashInsert(24680) == "24680"
    assert DashInsert(7777777) == "7-7-7-7-7-7-7"
    print("All test cases pass")

test_DashInsert()
