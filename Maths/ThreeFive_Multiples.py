"""
Have the function ThreeFiveMultiples(num) return the sum of all the 
multiples of 3 and 5 that are below num. For example: if num is 10, 
the multiples of 3 and 5 that are below 10 are 3, 5, 6, and 9, 
and adding them up you get 23, so your program should return 23. 
The integer being passed will be between 1 and 100.

Examples
Input: 6
Output: 8
Input: 1
Output: 0
"""

def ThreeFiveMultiples(num):
    # initialize sum to zero
    sum = 0
    # iterate over all numbers less than num
    for i in range(num):
        # if i is a multiple of 3 or 5, add it to the sum
        if i % 3 == 0 or i % 5 == 0:
            sum += i
    return sum


# This function initializes the sum to zero, and then iterates 
# over all numbers less than `num`. For each number `i`, 
# if it is a multiple of 3 or 5, it adds it to the sum. 
# Finally, it returns the sum.


print(ThreeFiveMultiples(1)) # 0
print(ThreeFiveMultiples(6))# 8
print(ThreeFiveMultiples(10))# 23
print(ThreeFiveMultiples(15)) # 45
print(ThreeFiveMultiples(20)) # 78
 