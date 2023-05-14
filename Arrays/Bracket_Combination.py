"""
Problem Statement                                            
  Have the function BracketCombinations(num) read num which    
  will be an integer greater than or equal to zero, and return 
  the number of valid combinations that can be formed with num 
  pairs of parentheses.                                        
                                                               
  For example, if input is 3, then the possible combinations   
  of 3 pairs of parenthesis,                                   
  namely: ()()(), are ()()(), ()(()), (())(), ((())), & (()()) 
                                                               
  There are 5 total combinations when the input is 3, so your  
  program should return 5.                                     
                                                               
  Examples                                                     
  Input 1: 3                                                   
  Output 1: 5                                                  
                                                               
  Input 2: 2                                                   
  Output 2: 2 
"""

"""
Algorithm:
- We can solve this problem using recursive approach.
- We can maintain the count of open and close brackets.
- For each recursive call, we can add an open bracket if the count of open brackets is less than n, and add a close bracket if the count of close brackets is less than the count of open brackets.
- We can keep calling the recursive function with updated counts until we have used all the n pairs of parentheses.
- At each recursive call, we can check if we have used all n pairs of parentheses, and if yes, then we can increment the count of valid combinations by 1.
- Finally, we can return the count of valid combinations.
"""


def BracketCombinations(num):
    def generate_combinations(open_count, close_count):
        nonlocal count
        if open_count == num and close_count == num:
            count += 1
            return
        if open_count < num:
            generate_combinations(open_count+1, close_count)
        if close_count < open_count:
            generate_combinations(open_count, close_count+1)
        
    count = 0
    generate_combinations(0, 0)
    return count



print(BracketCombinations(0)) 
print(BracketCombinations(1)) 
print(BracketCombinations(2)) 
print(BracketCombinations(3)) 
print(BracketCombinations(4)) 

