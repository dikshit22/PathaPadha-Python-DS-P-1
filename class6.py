#Program to search for a value in a dictionary.
print('#Program-1')
d = {2: 'a', 3+4j: 7.7, 'Hi': 4j, 4.4: 1}
srch = eval(input('Enter the value to be searched: '))
for i in d:
    if d[i] == srch:
        print('\t', srch, 'is found with key', i)
        break
else:
    print('\t', srch, 'did not found')
    
   
#Program to take five keys as input which should be numbers. The values should be the
#square of those keys and then map it to the dictionary.
print('\n\n#Program-2')
d = {}
print('Enter the keys-')
for i in range(0, 5):
    k = int(input())
    d[k] = k**2
print('\tRequired dictionary is:', d)


#Program to sort (ascending and descending) a dictionary by value.
print('\n\n#Program-3')
d = {'a': 4, 2: 1.1, 3+4j: 3, 2.2: 1}
print('\tDictionary sorted by value in')
print('\t(a) ascending order:', sorted(d.values()))
print('\t(b) descending order:', sorted(d.values(), reverse = True))


#Program to concatenate following dictionaries to create a new one
#Sample Dictionary :
#dic1={1:10, 2:20}
#dic2={3:30, 4:40}
#dic3={5:50,6:60}
#Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
print('\n\n#Program-4')
dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50, 6:60}
dic = dic1.copy()
dic.update(dic2)
dic.update(dic3)
print('\tNew dictionary is:', dic)


#Program to take a string as argument in the fucntion and display it in reverse
#order.
print('\n\n#Program-5')
def fun(string):
    print('\tGiven string in reverse order is:', s[::-1])

s = input('Enter the string argument: ')
fun(s)

'''
                OUTPUT
#Program-1
Enter the value to be searched: 7.7
         7.7 is found with key (3+4j)

Enter the value to be searched: 7
         7 did not found


#Program-2
Enter the keys-
2
4
6
8
10
	Required dictionary is: {2: 4, 4: 16, 6: 36, 8: 64, 10: 100}


#Program-3
        Dictionary sorted by value in
        (a) ascending order: [1, 1.1, 3, 4]
        (b) descending order: [4, 3, 1.1, 1]


#Program-4
	New dictionary is: {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}


#Program-5
Enter the string argument: Hello everyone
	Given string in reverse order is: enoyreve olleH
'''
