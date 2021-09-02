#Program to get a string made of the first 2 and the last 2 chars from a given
#string. If the string length is less than 2, print 'empty string'.
string = input("Enter a string:\t")
if(len(string) >= 2):
    newstr = string[:2]+string[-2:]
    print("\tThe new string is:", newstr)
else:
    print("\tEmpty string")

'''
                OUTPUT
Enter a string:	Hello
	The new string is: Helo

Enter a string:	Hit
	The new string is: Hiit

Enter a string:	Hi
	The new string is: HiHi

Enter a string:	H
	Empty string
'''
