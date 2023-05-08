"""
Problem Statement                                            
  Have the function BasicRomanNumerals(str) read str which     
  will be a string of Roman numerals. The numerals being used  
  are: I for 1, V for 5, X for 10, L for 50, C for 100, D for  
  500 and M for 1000. In Roman numerals, to create a number    
  like 11 you simply add a 1 after the 10, so you get XI. But  
  to create a number like 19, you use the subtraction notation 
  which is to add an I before an X or V (or add an X before    
  an L or C). So 19 in Roman numerals is XIX.                  
                                                               
  The goal of your program is to return the decimal equivalent 
  of the Roman numeral given. For example: if str is "XXIV"    
  your program should return 24                                
                                                               
  Examples                                                     
  Input 1: "IV"                                                
  Output 1: 4                                                  
                                                               
  Input 2: XLVI                                                
  Output 2: 46          
"""

"""                        Algorithm

Algorithm:
1. Initialize a dictionary that maps Roman numerals to their decimal values
2. Initialize a variable called "result" to 0
3. Iterate through the string of Roman numerals from left to right:
     a. Get the decimal value of the current numeral using the dictionary
     b. If the next numeral (if it exists) has a higher value than the current numeral, subtract the current value from the result
     c. Otherwise, add the current value to the result
4. Return the result

"""
def BasicRomanNumerals(str):
    roman_to_decimal = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    result = 0
    for i in range(len(str)):
        current_value = roman_to_decimal[str[i]]
        if i < len(str) - 1 and roman_to_decimal[str[i+1]] > current_value:
            result -= current_value
        else:
            result += current_value
    return result

def test_BasicRomanNumerals():
    assert BasicRomanNumerals("IV") == 4
    assert BasicRomanNumerals("XLVI") == 46
    assert BasicRomanNumerals("XIX") == 19
    assert BasicRomanNumerals("MMXXI") == 2021
    assert BasicRomanNumerals("DCCCXC") == 890
    print("All test cases pass")

test_BasicRomanNumerals()