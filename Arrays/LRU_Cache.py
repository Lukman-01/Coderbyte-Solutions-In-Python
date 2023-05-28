"""
Problem Statement                                            
  Have the function LRUCache( strArr ) take the array of       
  characters stored in strArr, which will contain characters   
  ranging from A to Z in some arbitrary order, and determine   
  what elements still remain in a virtual cache that can hold  
  up to 5 elements with an LRU cache algorithm implemented.    
                                                               
  For example: if strArr is ["A","B","C","D","A","E","D","Z"], 
  then the following steps are taken:                          
                                                               
  1) "A" doesn't exist in the cache, so store it in the cache  
  2) "B" doesn't exist in the cache, so store it in the cache  
  So far the cache contains: ["A", "B"].                       
  3) "C" doesn't exist in the cache, so store it in the cache  
  4) "D" doesn't exist in the cache, so store it in the cache  
  So far the cache contains: ["A", "B", "C", "D"].             
  5) Now A is accessed again, but it exists in th cache already
  so it is brought to the front: ["B", "C", "D", "A"].         
  6) "E" doesn't exist in the cache, so store it in the cache  
  So far the cache contains: ["B", "C", "D", "A", "E"].        
  7) D is accessed again so its brought to the front as follows
  So far the cache contains: ["B", "C", "A", "E", "D"].        
  8) Z does not exist in the cache so add it to the front &    
  remove the least recently used element                       
  So far the cache contains: ["C", "A", "E", "D", "Z"].        
                                                               
  Now the caching steps have been completed and your program   
  should return the order of the cache with the elements joined
  into a string, separated by a hyphen. Therefore, for the     
  example above your program should return C-A-E-D-Z.          
                                                               
  Examples                                                     
  Input 1: ["A", "B", "A", "C", "A", "B"]                      
  Output 1: C-A-B                                              
                                                               
  Input 2: ["A", "B", "C", "D", "E", "D", "Q", "Z", "C"]       
  Output 2: E-D-Q-Z-C         
"""

# Type of Algorithm: LRU Cache Algorithm

# Algorithm:
# 1. Create an empty cache list
# 2. Traverse through each element in the input array:
#       a. Check if the element is already in the cache list, if it exists, remove the element
#          from the cache list.
#       b. Append the element to the front of the cache list.
#       c. If the length of the cache list exceeds 5, remove the last element from the cache list.
# 3. Join the elements in the cache list into a string separated by a hyphen.

 

def LRUcache(strArr):
    cache = []
    for element in strArr:
        if element in cache:
            cache.remove(element)
        cache.insert(0, element)
        if len(cache) > 5:
            cache.pop()
    return '-'.join(cache)

print(LRUcache(["A", "B", "A", "C", "A", "B"]))  # C-A-B
print(LRUcache(["A", "B", "C", "D", "E", "D", "Q", "Z", "C"]))  # E-D-Q-Z-C
print(LRUcache(["A","B","C","D","A","E","D","Z"]))  # C-A-E-D-Z
print(LRUcache(["A","B","A","C","A","B","C","A","D","B","E"]))  # E-D-B-A-C
print(LRUcache(["A","B","C","D","A","E","D","Z","D","C","E","Z"]))  # Z-E-C-D-A

 