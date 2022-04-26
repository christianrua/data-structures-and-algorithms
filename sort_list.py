l1 = [0,3,4,31]
l2 = [4,6,30]

def merge_sorted_arrays(list1, list2):
    merge_list = list1 + list2
    merge_list.sort()
    return merge_list

print(merge_sorted_arrays(l1,l2))    