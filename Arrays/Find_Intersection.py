"""
Have the function FindIntersection(strArr) read the array 
of strings stored in strArr which will contain 2 elements: 
the first element will represent a list of comma-separated 
numbers sorted in ascending order, the second element will 
represent a second list of comma-separated numbers (also sorted). 
Your goal is to return a comma-separated string containing the 
numbers that occur in elements of strArr in sorted order. 
If there is no intersection, return the string false.

Examples
Input: ["1, 3, 4, 7, 13", "1, 2, 4, 13, 15"]
Output: 1,4,13

Input: ["1, 3, 9, 10, 17, 18", "1, 4, 9, 10"]
Output: 1,9,10
"""

# Algorithm:
# 1. Define a function called `FindIntersection` that takes one parameter `strArr`.
# 2. Split `strArr` into two separate lists using the comma as a delimiter.
# 3. Convert the strings in the two lists into sets of integers.
# 4. Find the intersection between the two sets using the `intersection` method.
# 5. If the intersection set is empty, return the string "false".
# 6. Sort the intersection set in ascending order.
# 7. Convert the sorted intersection set back into a comma-separated string.
# 8. Return the sorted comma-separated string.

 

def FindIntersection(strArr):

  # code goes here
  l1 = set(map(int, strArr[0].split(",")))
  l2 = set(map(int, strArr[1].split(",")))

  intersection = l1.intersection(l2)

  if(len(intersection) == 0):
    return False
  else:
    sinter = sorted(intersection)
    return ",".join(map(str, sinter))
 


print(FindIntersection(["1, 3, 4, 7, 13", "1, 2, 4, 13, 15"]))  # Output: 1,4,13
print(FindIntersection(["1, 3, 9, 10, 17, 18", "1, 4, 9, 10"]))  # Output: 1,9,10
print(FindIntersection(["1, 2, 3", "4, 5, 6"]))              # Output: false
#print(FindIntersection(["", "1, 2, 3, 4"]))                   # Output: false
#print(FindIntersection(["1, 2, 3", ""]))                      # Output: false

