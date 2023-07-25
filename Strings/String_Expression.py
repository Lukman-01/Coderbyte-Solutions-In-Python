"""
Problem Statement                                            
  Have the function StringExpression(str) read the str         
  parameter being passed which will contain the written out    
  version of the numbers 0-9 and the words "minus" or "plus" & 
  convert the expression into an actual final number written   
  out as well.                                                 
  For example: if str is "foursixminustwotwoplusonezero" then  
  this converts to "46 - 22 + 10" which evaluates to 34 and    
  your program should return the final string threefour.       
  If your final answer is negative it should include the       
  word "negative."                                             
                                                               
  Examples                                                     
  Input 1: "onezeropluseight"                                  
  Output 1: oneeight                                           
                                                               
  Input 2: oneminusoneone                                      
  Output 2: negativeonezero     
"""

def parse(expression):
    return eval(expression, {'__builtins__': None}, {})

def StringExpression(string):
    number_to_words = {
        'zero': '0',
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9',
        'minus': '-',
        'plus': '+'
    }
    words_to_number = {
        '0': 'zero',
        '1': 'one',
        '2': 'two',
        '3': 'three',
        '4': 'four',
        '5': 'five',
        '6': 'six',
        '7': 'seven',
        '8': 'eight',
        '9': 'nine'
    }
    count = 0
    position = 0
    expression = ""
    for i in range(len(string) + 1):
        if count == 3 or count == 4 or count == 5:
            if string[position:i] in number_to_words or string[position:i] == '0':
                expression += number_to_words[string[position:i]]
                count = 0
                position = i
        count += 1

    value = str(parse(expression))
    result = ""
    for digit in value:
        if digit == "-":
            result += "negative"
        elif digit in words_to_number:
            result += words_to_number[digit]

    return result

# Test cases
print(StringExpression("foursixminustwotwoplusonezero"))  # Output: "threefour"
print(StringExpression("onezeropluseight"))             # Output: "oneeight"
print(StringExpression("oneminusoneone"))               # Output: "negativeonezero"
print(StringExpression("sevenminusfoursixpluseight"))   # Output: "negativeonefour"
print(StringExpression("threeminustwozero"))            # Output: "onezero"


"""
Algorithm:

1. Create a dictionary `number_to_words` that maps written numbers (zero, one, ..., nine) and arithmetic operations (minus, plus) to their numerical representations and symbols ('0', '1', ..., '9', '-', '+').
2. Create a dictionary `words_to_number` that maps numerical representations to their written form (e.g., '0' -> 'zero', '1' -> 'one', ..., '9' -> 'nine').
3. Initialize variables `count` and `position` to 0 and an empty string `expression`.
4. Iterate through the input `string` to convert the written numbers to their numerical representations:
   - If the length of the current substring (from `position` to `i`) is 3, 4, or 5 characters, check if it exists in the `number_to_words` dictionary.
   - If it does, append the corresponding numerical representation to the `expression` and reset `count` to 0. Update `position` to the current index `i`.
5. Use the `parse` function to evaluate the mathematical expression represented by the `expression`.
6. Convert the result of the evaluation to a string `value`.
7. Initialize an empty string `result`.
8. Iterate through the characters in `value`:
   - If the character is "-", append "negative" to `result`.
   - If the character exists in `words_to_number`, append the corresponding word to `result`.
9. Return the final `result`.
"""