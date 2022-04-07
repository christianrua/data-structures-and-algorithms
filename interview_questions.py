# Given two arrays, make a function that detects if there is some common items between the two.

array1 = ['a','b','c','x']
array2 = ['z','y','i']

array3 = ['a','b','c','x']
array4 = ['z','y','x']

def common_items(l1,l2):
    if len(l1) > len(l2):
        shortest_list = set(l2)
        longest_list = set(l1)
    else:
        shortest_list = set(l1)  
        longest_list = set(l2)  
        
    for item in shortest_list:
        if item in longest_list:
            return True
    return False        

print(common_items(array1,array2))
print(common_items(array3,array4))

def common_items_better(l1,l2):
    if len(l1) > len(l2):
        biggest_list_dict = {i:True for i in l1}
        shortest_list = l2
    else: 
        biggest_list_dict = {i:True for i in l2}  
        shortest_list = l1

    for item in shortest_list:
        if biggest_list_dict[item] == True:
            return True
            
    return False 

