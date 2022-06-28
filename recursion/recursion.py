

counter = 0
def inception(counter):
    if counter > 4:
        return 'done!'

    counter += 1
    return inception(counter)

#print(inception(counter))

"""
Given a number N return the index value of the Fibonacci sequence, where the sequence is:

0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144 ...

The pattern of the secuence is that each value is the sum of the 2 previous values, that means that 
for N=5 -> 2 + 3
"""

def fibonacciIterativeRecursive(index, num1=0,num2=1):
    if index == 1:
        return num2
    return fibonacciIterativeRecursive(index-1, num1=num2, num2=num1+num2)

print(fibonacciIterativeRecursive(8))        