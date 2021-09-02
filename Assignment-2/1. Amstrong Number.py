#Program to find whether a number is amstrong number or not.
n = int(input("Enter a number:\t"))
d = n
s = 0
while((d%10) != 0):
    s+= (d%10)**3
    d = d//10
if(s == n):
    print('\t', n, 'is an amstrong number')
else:
    print('\t', n, 'is not an amstrong number')
    
'''
                OUTPUT
Enter a number:	153
	 153 is an amstrong number

Enter a number:	154
         154 is not an amstrong number
'''
