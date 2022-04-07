def booo(n):
    for i in range(n+1):
        print('boooo')

#print(booo(5)) #space complexity of O(1)

def arrayOfHiNTimes(n):
    hiArray = []
    for i in range(n):
        hiArray.append('hi')
    return hiArray    

print(arrayOfHiNTimes(5)) #space complexity of O(n)