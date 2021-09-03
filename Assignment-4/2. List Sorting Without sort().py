#Program to sort a list without using sort()
l = eval(input('Enter the unsorted list: '))
for i in range(0, len(l)):
    low = l[i]
    k = i
    for j in range(i+1, len(l)):
        if(l[j] < low):
            low = l[j]
            k = j
    l[k] = l[i]
    l[i] = low
    
print('\tThe sorted list is:', l)
    
'''
                OUTPUT
Enter the unsorted list: [5, 2, 4, 1, 7, 3, 9, 6, 8]
	The sorted list is: [1, 2, 3, 4, 5, 6, 7, 8, 9]

Enter the unsorted list: [7, 1, 9, 4, 2, 5, 3, 8, 5, 6]
	The sorted list is: [1, 2, 3, 4, 5, 5, 6, 7, 8, 9]
'''
