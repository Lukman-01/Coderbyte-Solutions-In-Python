"""
Problem Statement                                            
  Have the function CountingAnagrams(str) take the str         
  parameter & determine how many anagrams exist in the string. 
  An anagram is a new word that is produced from rearranging   
  the characters in a different word.                          
  For example: cars and arcs are anagrams.                     
                                                               
  Your program should determine how many anagrams exist in a   
  given string and return the total number.                    
                                                               
  For example: "cars are very cool so are arcs and my os"      
  then your program should return 2 because "cars" and "arcs"  
  form 1 anagram and "so" and "os" form a 2nd anagram.         
                                                               
  The word "are" occurs twice in the string but it isn't an    
  anagram because it is the same word just repeated.           
  The string will contain only spaces and lowercase letters,   
  no punctuation, numbers, or uppercase letters.               
                                                               
  Examples                                                     
  Input 1: "aa aa odg dog gdo"                                 
  Output 1: 2                                                  
                                                               
  Input 2: "a c b c run urn urn"                               
  Output 2: 1        
"""


"""
Algorithm:

1. Initialize an empty hash table `word_freq` to store the frequency of each word.
2. Split the input string `str` into individual words using the space character as the delimiter.
3. Iterate through each word:
     - Remove any leading or trailing whitespace from the word.
     - Sort the characters of the word in alphabetical order to standardize its representation.
     - If the sorted word already exists in `word_freq`, increment its frequency by 1.
     - If the sorted word does not exist in `word_freq`, add it as a new key with a frequency of 1.
4. Initialize a variable `anagram_count` to 0.
5. Iterate through the values of `word_freq`:
     - If the frequency of a word is greater than 1 and not equal to the length of the word itself (indicating a repeated word), increment `anagram_count` by the combination of the frequency value taken 2 at a time (nCr formula: n! / (r! * (n-r)!), where n is the frequency and r is 2).
6. Return `anagram_count` as the result.
"""
 

import math

def CountingAnagrams(str):
    word_freq = {}

    words = str.split()

    for word in words:
        word = word.strip()
        sorted_word = ''.join(sorted(word))
        if sorted_word in word_freq:
            word_freq[sorted_word] += 1
        else:
            word_freq[sorted_word] = 1

    anagram_count = 0

    for freq in word_freq.values():
        if freq > 1 and freq != len(word_freq):
            anagram_count += math.comb(freq, 2)

    return anagram_count
 
    

print(CountingAnagrams("aa aa odg dog gdo"))   
# Output: 2

print(CountingAnagrams("a c b c run urn urn"))   
# Output: 1
 