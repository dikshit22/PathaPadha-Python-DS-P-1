#Program to swap two numbers
#Using third variable
print("Swapping using third variable")
print('Enter two numbers:')
a, b = int(input('a = ')), int(input('b = '))
print("Before swapping:\na =", a, " b =", b)
c = a
a = b
b = c
print("After swapping:\na =", a, " b =", b)

#Without using third variable
print("\nSwapping without using third variable")
print('Enter two numbers:')
p, q = int(input('p = ')), int(input('q = '))
print("Before swapping:\np =", p, " q =", q)
p = p+q
q = p-q
p = p-q
print("After swapping:\np =", p, " q =", q)
