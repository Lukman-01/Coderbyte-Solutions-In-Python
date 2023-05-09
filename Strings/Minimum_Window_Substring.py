"""
Problem Statement                                            
  Have the function MinWindowSubstring(strArr) take the array  
  of strings stored in strArr, which will contain only two     
  strings, the first parameter being the string N and the      
  second parameter being a string K of some characters, and    
  your goal is to determine the smallest substring of N that   
  contains all the characters in K.                            
                                                               
  For example: if strArr is ["aaabaaddae", "aed"] then the     
  smallest substring of N that contains the characters         
  a, e, and d is "dae" located at the end of the string.       
  So for this example your program should return the string    
                                                               
  Another example: if strArr is ["aabdccdbcacd", "aad"] then   
  the smallest substring of N that contains all of the         
  characters in K is "aabd" which is located at the beginning  
  of the string. Both parameters will be strings ranging in    
  length from 1 to 50 characters and all of K's characters will
  exist somewhere in the string N. Both strings will only      
  contains lowercase alphabetic characters.                    
                                                               
  Examples                                                     
  Input 1: ["ahffaksfajeeubsne", "jefaa"]                      
  Output 1: aksfaje                                            
                                                               
  Input 2: ["aaffhkksemckelloe", "fhea"]                       
  Output 2: affhkkse     
"""
"""
Algorithm:
1. Initialize a variable "min_len" to a very large value.
2. Initialize a dictionary "char_count" to keep count of all characters in K and its count in N.
3. Initialize two pointers "start" and "end" at index 0 in the string N.
4. Traverse the string N and for each character c, do the following:
   a. Check if c is in K, if not continue to the next character.
   b. If c is in K, update the count of c in the char_count dictionary.
   c. If the count of c in char_count is less than or equal to its count in K, update a variable "matched_count" to keep count of the number of matched characters in K.
   d. If matched_count equals the length of K, it means all characters in K are matched, so shrink the window from the start to remove extra characters.
   e. While shrinking the window, if the character at start is not in K or its count in char_count is greater than its count in K, decrement its count in char_count and move the start pointer one step ahead.
   f. Update the length of the minimum window if it is smaller than the current length.
5. Return the minimum window substring.
"""

def MinWindowSubstring(strArr):
    # Store the two input strings in separate variables
    n, k = strArr
    
    # Initialize variables to keep track of the smallest window found so far,
    # the number of characters in k that still need to be found in the current window,
    # and the left and right indices of the current window
    smallest_window = None
    chars_remaining = len(k)
    left_index = right_index = 0
    
    # Initialize a dictionary to keep track of the frequency of characters in k
    # (since k may contain duplicate characters)
    k_chars_freq = {}
    for char in k:
        k_chars_freq[char] = k_chars_freq.get(char, 0) + 1
    
    # Iterate over the characters in n, expanding the window to the right
    for i, char in enumerate(n):
        if char in k_chars_freq:
            # If the current character is in k, decrement the number of characters
            # that still need to be found in the current window
            k_chars_freq[char] -= 1
            if k_chars_freq[char] >= 0:
                chars_remaining -= 1
        
        # If all characters in k have been found in the current window,
        # try to shrink the window from the left
        if chars_remaining == 0:
            while True:
                # Get the character at the left index of the current window
                left_char = n[left_index]
                
                if left_char in k_chars_freq:
                    # If the left character is in k, increment the number of characters
                    # that still need to be found in the current window
                    k_chars_freq[left_char] += 1
                    if k_chars_freq[left_char] > 0:
                        chars_remaining += 1
                
                # Shrink the window by moving the left index to the right
                left_index += 1
                
                # If the window no longer contains all characters in k, break out of the loop
                if chars_remaining > 0:
                    break
            
            # Check if the current window is smaller than the smallest window found so far
            if smallest_window is None or i - left_index + 1 < len(smallest_window):
                smallest_window = n[left_index-1:i+1]
    
    # Return the smallest window found
    return smallest_window

print(MinWindowSubstring(["aaabaaddae", "aed"]))  # should print "dae"
print(MinWindowSubstring(["aabdccdbcacd", "aad"]))  # should print "aabd"
print(MinWindowSubstring(["ahffaksfajeeubsne", "jefaa"]))  # should print "aksfaje"
print(MinWindowSubstring(["aaffhkksemckelloe", "fhea"]))  # should print "affhkkse"
