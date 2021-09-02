#Program to change a given string to a new string where the first and last chars
#have been exchanged. 
string = input("Enter a string:\t")
string = string[-1]+string[1:-1]+string[0]
print("\tThe new string is:", string)

'''
                OUTPUT
Enter a string:	Hello
	The new string is: oellH
'''
