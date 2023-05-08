"""
Problem Statement                                            
  Have the function DifferentCases(str) take the str parameter 
  being passed and return it in upper camel case format where  
  the first letter of each word is capitalized. The string will
  only contain letters and some combination of delimiter       
  punctuation characters separating each word.                 
                                                               
  Examples                                                     
  Input 1: "Daniel LikeS-coding"                               
  Output 1: DanielLikesCoding                                  
                                                               
  Input 2: "cats AND*Dogs-are Awesome"                         
  Output 2: CatsAndDogsAreAwesome                              
                                                               
  Input 3: "a b c d-e-f%g"                                     
  Output 3: ABCDEFG          
"""

"""
Here's the outline of the algorithm for the `DifferentCases` function:

1. Convert the input string `str` to lowercase.
2. Split the string into words using delimiter punctuation characters.
3. Capitalize the first letter of each word.
4. Concatenate the capitalized words to form the output string.
"""

import re

def DifferentCases(strparam):
    # convert str to lowercase
    strparam = strparam.lower()
    # split the string into words using delimiter punctuation characters
    words = re.split('[\W_]+', strparam)
    # capitalize the first letter of each word and concatenate the result
    return ''.join([word.capitalize() for word in words])



def test_DifferentCases():
    assert DifferentCases("Daniel LikeS-coding") == "DanielLikesCoding"
    assert DifferentCases("cats AND*Dogs-are Awesome") == "CatsAndDogsAreAwesome"
    assert DifferentCases("a b c d-e-f%g") == "ABCDEFG"
    assert DifferentCases("Hello world!") == "HelloWorld"
    assert DifferentCases("Python is fun") == "PythonIsFun"
    print("All test cases pass")

test_DifferentCases()
