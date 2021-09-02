#Program to add 'ing' at the end of a given string (length should be at least 3).
#If the given string already ends with 'ing' then add 'ly' instead. If the
#string length of the given string is less than 3, leave it unchanged. 
string = input("Enter a string:\t")
if(len(string) >= 3):
    if(string[-3:] != 'ing'):
        string = string+'ing'
    else:
        string = string+'ly'
    print("\tThe new string is:", string)
else:
    print("\tThe string is:", string)

'''
                OUTPUT
Enter a string:	Help
	The new string is: Helping

Enter a string:	Loving
	The new string is: Lovingly

Enter a string:	Do
	The string is: Do
'''
