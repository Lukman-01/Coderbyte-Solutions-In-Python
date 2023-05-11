"""
Histogram Area
Have the function HistogramArea(arr) read the array of non-negative 
integers stored in arr which will represent the heights of bars on 
a graph (where each bar width is 1), and determine the largest area 
underneath the entire bar graph. For example: if arr is [2, 1, 3, 4, 1] 
then this looks like the following bar graph:



You can see in the above bar graph that the largest area underneath 
the graph is covered by the x's. The area of that space is equal to 
6 because the entire width is 2 and the maximum height is 3, 
therefore 2 * 3 = 6. Your program should return 6. 
The array will always contain at least 1 element.

Examples
Input: [6, 3, 1, 4, 12, 4]
Output: 12
Input: [5, 6, 7, 4, 1]
Output: 16
"""
"""
Algorithm:
1. Initialize a stack to store indices of the bars and 
    a variable called max_area to store the maximum area.
2. Iterate through each bar in the array:
   a. If the stack is empty or the height of the current 
        bar is greater than or equal to the height of the bar at 
        the top of the stack, push the index of the current bar to the stack.
   b. Otherwise, keep popping indices from the stack until 
        either the stack is empty or the height of the bar at the 
        top of the stack is less than the height of the current bar. 
        For each popped index, calculate the area of the rectangle 
        using the popped index as the right boundary, the height of 
        the bar at the popped index as the height, and the left 
        boundary as the index at the top of the stack (or -1 if the stack is empty). 
        Update max_area if the calculated area is greater than max_area.
3. After iterating through all bars in the array, repeat step 2b for any 
        remaining indices on the stack until the stack is empty.
"""

def HistogramArea(arr):
    stack = []
    max_area = 0
    for i, h in enumerate(arr):
        while stack and arr[stack[-1]] > h:
            height = arr[stack.pop()]
            width = i if not stack else i - stack[-1] - 1
            area = height * width
            max_area = max(max_area, area)
        stack.append(i)
    while stack:
        height = arr[stack.pop()]
        width = len(arr) if not stack else len(arr) - stack[-1] - 1
        area = height * width
        max_area = max(max_area, area)
    return max_area



Input1= [2, 1, 3, 4, 1]
print(HistogramArea(Input1))

Input2= [6, 3, 1, 4, 12, 4]
print(HistogramArea(Input2))

Input3= [5, 6, 7, 4, 1]
print(HistogramArea(Input3))

Input4= [1]
print(HistogramArea(Input4))

Input5= [0, 0, 0, 0, 0, 0]
print(HistogramArea(Input5))
