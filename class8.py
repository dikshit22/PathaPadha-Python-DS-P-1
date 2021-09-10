#Program to create a module named temp where you have to create a function to
#convert temp from celsius to fahrenheit and then in another module call this
#function by taking temp as input. Use function with arguments.
print('#Program-1')
t = int(input('Enter the temperature in celcius: '))
import temp
print('\tTemperature in fahrenheit is:', temp.celciusToFahrenheit(t))


#Program to create a lambda function that adds 15 to a given number passed in as
#an argument.
print('\n\n#Program-2')
result = lambda x: x+15
print('Result is:', result(5))


#Program to capitalize the first letter of all the strings in a list using
#lambda function.
print('\n\n#Program-3')
l = ['hello', 'everyone', 'how', 'are', 'you?']
result = map(lambda s: s.capitalize(), l)
print('New list is:', list(result))


#Program to sort a list of dictionaries using Lambda.
print('\n\n#Program-4')
models = [{'make':'Nokia', 'model':216, 'color':'Black'},
          {'make':'Mi Max', 'model':2, 'color':'Gold'},
          {'make':'Samsung', 'model': 7, 'color':'Blue'}]
res = sorted(models, key = lambda x:x['model'])
print('Sorted list is:', list(res))

'''
                OUTPUT
#Program-1
Enter the temperature in celcius: -40
	Temperature in fahrenheit is: -40.0


#Program-2
Result is: 20


#Program-3
New list is: ['Hello', 'Everyone', 'How', 'Are', 'You?']


#Program-4
Sorted list is: [{'make': 'Mi Max', 'model': 2, 'color': 'Gold'},
{'make': 'Samsung', 'model': 7, 'color': 'Blue'},
{'make': 'Nokia', 'model': 216, 'color': 'Black'}]
'''
