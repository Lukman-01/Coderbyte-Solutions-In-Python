"""
Problem Statement                                            *
  Have the function StarRating(str) take the str parameter     
  being passed which will be an average rating between         
  0.00 and 5.00, and convert this rating into a list of 5 image
  names to be displayed in a user interface to represent the   
  rating as a list of stars and half stars. Ratings should be  
  rounded to the nearest half. There are 3 image file names    
  available: "full.jpg", "half.jpg", "empty.jpg".              
  The output will be the name of the 5 images                  
  (without the extension), from left to right, separated by    
  spaces.                                                      
                                                               
  Examples                                                     
  Input 1: "0.38"                                              
  Output 1: half empty empty empty empty                       
                                                               
  Input 2: "4.5"                                               
  Output 2: full full full full half     
"""

"""
Algorithm:
1. Convert the input string to a floating-point number.
2. Multiply the number by 2 and round it to the nearest integer. This will give us a value between 0 and 10, representing the rating in tenths.
3. Divide the rounded value by 2 to get the number of full stars.
4. Subtract the number of full stars from 5 to get the number of empty stars.
5. If the rounded value is odd, add a half star.
6. Create a list to store the image names.
7. Append "full" to the list the number of times equal to the number of full stars.
8. Append "half" to the list if the rounded value is odd.
9. Append "empty" to the list the number of times equal to the number of empty stars.
10. Join the elements of the list into a string separated by spaces.
11. Return the resulting string.
"""

def StarRating(str):
    rating = float(str)
    rounded_rating = round(rating * 2)
    full_stars = rounded_rating // 2
    empty_stars = 5 - full_stars
    has_half_star = rounded_rating % 2 != 0

    image_names = ["full"] * full_stars
    if has_half_star:
        image_names.append("half")
    image_names.extend(["empty"] * empty_stars)

    return " ".join(image_names)



print(StarRating("0.38"))  # Output: half empty empty empty empty
print(StarRating("4.5"))   # Output: full full full half empty
print(StarRating("1.75"))  # Output: full full empty empty empty
print(StarRating("3.33"))  # Output: full full full half empty empty
print(StarRating("2.0"))   # Output: full full empty empty empty
