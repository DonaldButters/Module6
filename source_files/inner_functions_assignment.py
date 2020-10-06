#inner_functions_assignment.py

def area(rekt):
    a = rekt[0] * rekt[1]
    return a

def perimeter(rekt):
    p = (rekt[0] * 2) + (rekt[1] * 2)
    return p

def square(rekt):
    c = rekt[0] == rekt[1]
    return c

def measurements(rekt):
    print('Please enter this the width and length of the rectangle: ')
    length = float(input('Length: '))
    width = float(input('Width: '))
    rekt.append(length)
    rekt.append(width)
    print('Perimeter = ' + str(perimeter(rekt))
          + ' - Area = ' + str(area(rekt)) +
          ' - Is this a square?  ' + str(square(rekt)))

rekt = []
measurements(rekt)

