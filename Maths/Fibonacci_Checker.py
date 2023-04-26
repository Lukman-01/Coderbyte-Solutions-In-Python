"""
Have the function FibonacciChecker(num) return the string yes if 
the number given is part of the Fibonacci sequence. This sequence 
is defined by: Fn = Fn-1 + Fn-2, which means to find Fn you add 
the previous two numbers up. The first two numbers are 0 and 1, 
then comes 1, 2, 3, 5 etc. If num is not in the Fibonacci sequence, 
return the string no.

Examples
Input: 34
Output: yes
Input: 54
Output: no
"""
import math

def FibonacciChecker(num):
    # check if num is a perfect square
    x = 5*num*num + 4
    y = 5*num*num - 4
    if int(math.sqrt(x))**2 == x or int(math.sqrt(y))**2 == y:
        return "yes"
    else:
        return "no"


# This code uses the fact that a number is part of the Fibonacci sequence
#  if and only if either 5*num^2 + 4 or 5*num^2 - 4 is a perfect square. 
#  This is a well-known property of the Fibonacci sequence.

 
# Test case 1: num = 0
result = FibonacciChecker(0)
expected_result = "yes"
if result == expected_result:
    print("Test case 1 PASSED")
else:
    print("Test case 1 FAILED")

# Test case 2: num = 1
result = FibonacciChecker(1)
expected_result = "yes"
if result == expected_result:
    print("Test case 2 PASSED")
else:
    print("Test case 2 FAILED")

# Test case 3: num = 2
result = FibonacciChecker(2)
expected_result = "yes"
if result == expected_result:
    print("Test case 3 PASSED")
else:
    print("Test case 3 FAILED")

# Test case 4: num = 34
result = FibonacciChecker(34)
expected_result = "yes"
if result == expected_result:
    print("Test case 4 PASSED")
else:
    print("Test case 4 FAILED")

# Test case 5: num = 54
result = FibonacciChecker(54)
expected_result = "no"
if result == expected_result:
    print("Test case 5 PASSED")
else:
    print("Test case 5 FAILED")
