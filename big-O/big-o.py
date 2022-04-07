import time 

#start_time = time.time()

nemo = ['nemo']
everyone = ['1','1','1','nemo','1','1','1','1','1','1']
large = ['nemo' for i in range(100000)]


def find_nemo(some_array):
    
    for item in some_array:
        if item == 'nemo':
            print('found NEMO!')
            break
    #print("--- %s seconds ---" % (time.time() - start_time))        

#find_nemo(large) # O(n) or Linear time

#O(1) - Constant time

boxes = [0,1,2,3,4,5]

def log_first_two_boxes(boxes):
    print(boxes[0])
    print(boxes[1])

log_first_two_boxes(boxes) #O(2)