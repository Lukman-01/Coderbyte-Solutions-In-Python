"""
Problem Statement                                             
  Have the function HTMLElements(str) read the str parameter    
  being passed which will be a string of HTML DOM elements and  
  plain text. The elements that will be used are: b, i, em,     
  div, p.                                                       
                                                                
  For example: if str is "<div><b><p>hello world</p></b></div>" 
  then this string of DOM elements is nested correctly so your  
  program should return the string true.                        
                                                                
  If a string is not nested correctly, return the first element 
  encountered where, if changed into a different element, would 
  result in a properly formatted string. If the string is not   
  formatted properly, then it will only be one element that     
  needs to be changed.                                          
                                                                
  For example: if str is "<div><i>hello</i>world</b>" then your 
  program should return the string div because if the first     
  <div> element were changed into a <b>, the string would be    
  properly formatted.                                           
                                                                
  Examples                                                      
  Input 1: "<div><div><b></b></div></p>"                        
  Output 1: div                                                 
                                                                
  Input 2: "<div>abc</div><p><em><i>test test test</b></em></p>"
  Output 2: i              
"""
"""
Here's one possible algorithm to solve this problem:

1. Create an empty stack to keep track of opening tags.
2. Create a variable `i` and initialize it to 0.
3. While `i` is less than the length of `str`, do the following:
   a. If the current character is an opening tag, push it onto the stack.
   b. If the current character is a closing tag, check if it matches the most recent opening tag on the stack. 
   If it does not match, return the name of the opening tag as the answer. If it matches, 
   pop the opening tag off the stack.
   c. Increment `i`.
4. If the stack is empty, return `true`, otherwise return the name of the topmost opening tag on the stack.

"""


def HTMLElements(str):
    stack = []
    i = 0
    while i < len(str):
        if str[i] == '<':
            tag_name = str[i+1:str.index('>', i+1)]
            if not tag_name.startswith('/'):
                stack.append(tag_name)
            else:
                opening_tag = stack.pop()
                if opening_tag != tag_name[1:]:
                    return opening_tag
            i += len(tag_name) + 2
        else:
            i += 1
    return 'true' if not stack else stack[-1]
 
print(HTMLElements("<div><div><b></b></div></p>")) # div
print(HTMLElements("<div>abc</div><p><em><i>test test test</b></em></p>")) # i
print(HTMLElements("<b><i><em></em></i></b>")) # true
print(HTMLElements("<div><p></div></p>")) # p
print(HTMLElements("<div><i>hello</i>world</b>")) # div

