#Program to input an element and search whether it exists in the list or not
#along with its position.
print("#Program-1")
l = [1, 3.5, "HELLO", True, 3+4j, 'a']
for j in range(1, 13):
    srch = eval(input("Enter the element to search:\t"))
    for i in range(0, len(l)):
        if srch == l[i]:
            print('\t', srch, 'exists at index', i)
            break
        elif i == l[len(l)-1]:
            print('\t', srch, 'is not existing')
    print()

#Program to find the common elements between two lists.
print("\n#Program-2")
l1 = [1, 2, 3, 4, 5]
l2 = [8, 3, 5, 9]
l3 = list()
for i in l1:
    for j in l2:
        if i == j:
            l3.append(i)
if l3:
    print('\tThe common elements are:', l3)
else:
    print('\tNo common elements are there!')
print()

#Program to do the square of all the elements in a list and store it in a new
#list and then display the new list.
print("\n#Program-3")
l4 = eval(input('Enter the list elements: '))
l5 = [i**2 for i in l4]
print('\tThe new list is:', l5)

'''
                OUTPUT
#Program-1
Enter the element to search:	'HELLO'
         HELLO exists at index 2
         
Enter the element to search:	3+4j
         (3+4j) exists at index 4
         
Enter the element to search:	'a'
         a exists at index 5
         
Enter the element to search:	3.5
         3.5 exists at index 1
         
Enter the element to search:	1
         1 exists at index 0
         
Enter the element to search:	2
         2 is not existing
         
Enter the element to search:	4.5
         4.5 is not existing
         
Enter the element to search:	'Hello'
         Hello is not existing
         
Enter the element to search:	True
         True exists at index 3
         
Enter the element to search:	False
         False is not existing
         
Enter the element to search:	5+4j
         (5+4j) is not existing
         
Enter the element to search:	'b'
         b is not existing


#Program-2
	The common elements are: [3, 5]


#Program-3
Enter the list elements: 3, 4, 5, 6, 7, 8
	The new list is: [9, 16, 25, 36, 49, 64]
'''
