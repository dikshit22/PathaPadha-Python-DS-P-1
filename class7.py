#Program to check for a perfect number using user defined function.
print('#Program-1')
def perfect(num):
    s = 1
    for i in range(2, num):
        if num % i == 0:
            s+= i
    if s == num:
        print('\t', num, 'is a perfect number\n')
    else:
        print('\t', num, 'is not a perfect number\n')
        
perfect(int(input('Enter the number to check: ')))
perfect(int(input('Enter the number to check: ')))


#Program to get average of marks using function in function.
print('\n#Program-2')
def sum(*args):
    s = 0
    for i in args:
        s+= i
    return s

def avrg(*args):
    total = sum(*args)/len(args)
    print('\tAverage marks is:', total)

n = int(input('Enter the number of marks: '))
avrg(*(int(input()) for i in range(0, n)))


#Program to get function imported from module to print random float values in the
#range of 15 to 30.
print('\n\n#Program-3')
from random import *
print('Random float values in the range of 15 to 30 are:')
for i in range(1, 11):
    print(random()*(30-15)+15)

'''
                OUTPUT
#Program-1
Enter the number to check: 27
         27 is not a perfect number

Enter the number to check: 28
         28 is a perfect number


#Program-2
Enter the number of marks: 5
67
89
94
75
88
        Average marks is: 82.6


#Program-3
Random float values in the range of 15 to 30 are:
29.538021204216193
16.5476682396399
22.277641008556976
23.482039046720743
24.90317227196209
15.863149258570584
29.254012862790894
24.572758592178264
15.693326027556497
19.098288082198195
'''
