from itertools  import combinations

boxes = [1,2,3,4,5]
list_combinations = list()

for n in range(len(boxes) + 1):
    list_combinations += list(combinations(boxes, n))

print(list_combinations)
