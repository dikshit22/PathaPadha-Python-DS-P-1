#Program to find the greatest number out of 3 numbers using nested if
print('#Program to find the greatest number out of 3 numbers')
print('Enter three numbers:')
n1, n2, n3 = int(input('n1 = ')), int(input('n2 = ')), int(input('n3 = '))
if(n1 > n2):
    if(n1 > n3):
        print('/tThe greatest number is', n1)
    else:
        print('/tThe greatest number is', n3)
else:
    if(n2 > n3):
        print('/tThe greatest number is', n2)
    else:
        print('/tThe greatest number is', n3)

#Program to find factorial of a number
print('\n#Program to find factorial of a number')
n = int(input("Enter the number to find its factorial:\nnumber = "))
fact = 1
for i in range(n, 0, -1):
    fact*=i
print('\tFactorial of', n, 'is:\n\t', n, '! =', fact)

#Program to check whether a number is prime or not
print('\n#Program to check whether a number is prime or not')
n = int(input("Enter the number to check:\nnumber = "))
i = 2
for i in range(2, n):
    if(n%i == 0):
        break
    else:
        continue
if(i == n-1):
    print('\t', n, "is a prime number")
else:
    print('\t', n, 'is not a prime number')

'''
                            OUTPUT
#Program to find the greatest number out of 3 numbers
Enter three numbers:
n1 = 22
n2 = 20
n3 = 19
        The greatest number is 22

#Program to find factorial of a number
Enter the number to find its factorial:
number = 9
        Factorial of 9 is:
         9 ! = 362880

#Program to check whether a number is prime or not
Enter the number to check:
number = 53
         53 is a prime number
'''
