#Program to print
#1
#2 3
#4 5 6
#7 8 9 10
#11 12 13 14 15
print('#Program-1')
i = 1
for rows in range(1, 6):
    for cols in range(1, rows+1):
        print(i, end = ' ')
        i+=1
    print( )
print( )

#Program to count number of uppercase and lowercase characters in a string.
print('#Program-2')
string = input('Enter the string:\t')
u, l = 0, 0
for i in string:
    if(i.isupper()):
        u+=1
    elif(i.islower()):
        l+=1
print("\t(a) Number of uppercase characters is", u)
print("\t(b) Number of lowercase characters is", l)
print( )

#Program to convert the characters which are in lowercase to uppercase and vice
#versa and then display the updated string.
print('#Program-3')
string = input('Enter the string:\t')
print('\tThe new string is:', end = ' ')
for i in range(0, len(string)):
    if(string[i].isupper()):
        print(string[i].lower(), end = '')
    else:
        print(string[i].upper(), end = '')
print( )

'''
                OUTPUT
#Program-1
1 
2 3 
4 5 6 
7 8 9 10 
11 12 13 14 15 

#Program-2
Enter the string:	HELLO Everyone
	(a) Number of uppercase characters is 6
	(b) Number of lowercase characters is 7

#Program-3
Enter the string:	HELLO Everyone
The new string is: hello eVERYONE
'''


