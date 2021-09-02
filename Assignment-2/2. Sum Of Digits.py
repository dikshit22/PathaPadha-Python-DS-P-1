#Program to print the sum of digits of a number.
n = int(input("Enter a number:\t"))
d = n
s = 0
while((d%10) != 0):
    s+= (d%10)
    d = d//10
print('\tThe sum of digits of', n, 'is', s)

'''
                OUTPUT
Enter a number:	153
	The sum of digits of 153 is 9
'''
