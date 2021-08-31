#Program to compute the distance between two points
print('Enter the co-ordinates of the first point:')
x1, y1 = int(input("x1 = ")), int(input("y1 = "))
print('Enter the co-ordinates of the second point:')
x2, y2 = int(input("x2 = ")), int(input("y2 = "))
d = (((x1-x2)**2)+((y1-y2)**2))**0.5
print('Distance =', d, 'units')
