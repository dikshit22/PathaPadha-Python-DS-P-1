#Program to delete an element from a tuple which is input from the user.
print('#Program-1')
t = eval(input('Enter the tuple: '))
dlt = int(input('Enter the element to delete: '))
l = list(t)
for i in l:
    if i == dlt:
        l.remove(i)
t1 = tuple(l)
print('\tThe new tuple is:', t1)
print()

#Program to find the unequal elements from two sets.
print('#Program-2')
s = {"red", "orange", 1, 3.5}
s1 = {2, 'True', 3.5, 'red'}
print('First set is:', s, '\nSecond set is:', s1)
print('\tThe required elements are:', end = '\n\t')
for i in s:
    if i not in s1:
        print(i, end = '\n\t')
for j in s1:
    if j not in s:
        print(j, end = '\n\t')

'''
                OUTPUT
#Program-1
Enter the tuple: (1, 2, 3, 4, 2, 6, 4, 5)
Enter the element to delete: 2
	The new tuple is: (1, 3, 4, 6, 4, 5)

#Program-2
First set is: {1, 'red', 3.5, 'orange'} 
Second set is: {'True', 2, 3.5, 'red'}
	The required elements are:
	1
	orange
	True
	2
'''
