#Program to find the highest element in a list
l = eval(input('Enter the list: '))
h = l[0]
for i in l:
    if(i > h):
        h = i
print('\tThe highest element in the list is:', h)

'''
                OUTPUT
Enter the list: [1, 4, 2, 6, 3, 5, 9, 7, 8]
	The highest element in the list is: 9
'''
