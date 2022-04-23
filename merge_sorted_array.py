l1 = [0,3,4,32]
l2 = [4,6,30]

def merge_sorted_array(list1, list2):
    if list1 == []:
        return list2
    elif list2 == []:
        return list1

    full_list = []
    full_list = list1 + list2
    print("inside the funtion, unsorted_full_list value: ", full_list)
    full_list.sort()
    print("sorted_list value: ", full_list)
    return full_list

print(merge_sorted_array(l1,l2))    
