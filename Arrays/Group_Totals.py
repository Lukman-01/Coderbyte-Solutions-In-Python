"""
Have the function GroupTotals(strArr) read in the strArr parameter 
containing key:value pairs where the key is a string and the value 
is an integer. Your program should return a string with new key:value 
pairs separated by a comma such that each key appears only once 
with the total values summed up.

For example: if strArr is ["B:-1", "A:1", "B:3", "A:5"] 
then your program should return the string A:6,B:2.

Your final output string should return the keys in alphabetical order. 
Exclude keys that have a value of 0 after being summed up.

Examples
Input: ["X:-1", "Y:1", "X:-4", "B:3", "X:5"]
Output: B:3,Y:1

Input: ["Z:0", "A:-1"]
Output: A:-1
"""

def GroupTotals(strArr):

  # code goes here
  total = {}

  for p in strArr:
    key, value = p.split(":")
    value = int (value)
    if key in total:
      total[key] += value
    else:
      total[key] = value

  result = []
  for key, value in total.items():
    if value != 0:
      result.append(f"{key}:{value}")

  return ",".join(sorted(result))

# Algorithm

# 1. Create an empty dictionary called `totals` to store the sum of values for each key.
# 2. Iterate over each key:value pair in the `strArr` input.
# 3. Split each pair into the key and value components.
# 4. Convert the value to an integer.
# 5. If the key already exists in the `totals` dictionary, add the value to the existing sum.
# 6. Otherwise, create a new key in the `totals` dictionary with the initial value.
# 7. Create an empty list called `result` to store the key:value pairs with non-zero values.
# 8. Iterate over each key:value pair in the `totals` dictionary.
# 9. If the value is non-zero, append the key:value pair to the `result` list.
# 10. Sort the `result` list alphabetically.
# 11. Join the elements of the `result` list with a comma to create the final output string.
# 12. Return the final output string.


#Test Case 1:
input3 = ["A:2", "B:3", "C:4", "A:-1", "C:-3"]
print(GroupTotals(input3))  # Output: B:3,A:1,C:1

#Test Case 2:
input4 = ["X:0", "Y:0", "Z:0"]
print(GroupTotals(input4))  # Output: 

#Test Case 3:
input5 = []
print(GroupTotals(input5))  # Output: 

#Test Case 4:
input6 = ["A:10", "B:-5", "C:7", "D:0"]
print(GroupTotals(input6))  # Output: B:-5,C:7,A:10

#Test Case 5:
input7 = ["Z:1", "Y:2", "X:-3", "Y:0", "Z:0", "X:0"]
print(GroupTotals(input7))  # Output: Y:2,Z:1,X:-3
