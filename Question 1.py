# Module to flat a nested list with multiple levels of nesting allowed. 
  
# input list 
nested_list = [[[2]], [4, [5, 6, [6], 6, 6, 6], 7]]  
  
# output list 
output = []
  
# function used for removing nested  
# lists in python.  
def flat_list(nested_list): 
    for i in nested_list: 
        if type(i) == list: 
            flat_list(i) 
        else: 
            output.append(i) 
  
# Driver code 
print ("The original list: ", nested_list) 
flat_list(nested_list)
print ("The list after removing nesting: ", output)
