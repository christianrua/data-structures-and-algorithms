"""
Google Question
Given an array = [2,5,1,2,3,5,1,2,4]
It should return 2

Given an array = [2,1,1,2,3,5,1,2,4]
It should return 1

Given an array = [2,3,4,5]
It should return undefined

"""
from collections import Counter


an_array = [2,3,4,5]
result = Counter(an_array)


def first_recurrent_character(some_array):
    items_set = set(some_array)
    ocurrences_by_item = Counter(some_array)
    repeated_items = {}

    for item in items_set:
        if ocurrences_by_item[item] > 1:
            repeated_items[item] = some_array.index(item)

    return repeated_items        


#print(first_recurrent_character(an_array))

def indices(lst, item):
    return [i for i, x in enumerate(lst) if x == item]

def first_recurrent_character2(some_array):  
    repeated_items_indexes = dict((x, indices(some_array, x)) for x in set(some_array) if some_array.count(x) > 1)   
    min_dist = 1000
    target_index = 500
    for key in repeated_items_indexes.keys():
        list_of_indexes = repeated_items_indexes[key]
        distance = list_of_indexes[1] - list_of_indexes[0]
        if distance < min_dist:
            min_dist = distance
            target_index = key
    
    if target_index == 500:
        return "undefined"
    else:
        target_index           

print(first_recurrent_character2(an_array))    