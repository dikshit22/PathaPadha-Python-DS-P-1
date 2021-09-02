#Program to print the sum of even and odd numbers in the range of 20 to 30
se, so = 0, 0
for i in range(20, 31):
    if((i%2) == 0):
        se+= i
    else:
        so+= i
print('\t(a) The sum of even numbers in the range of 20 to 30 is', se)
print('\t(b) The sum of odd numbers in the range of 20 to 30 is', so)

'''
                                    OUTPUT
        (a) The sum of even numbers in the range of 20 to 30 is 150
	(b) The sum of odd numbers in the range of 20 to 30 is 125
'''
