"""a function that calculate the area of these shapes:
triangle = (0.5 * base * height), rectangle = (width * height),
Circle= (PI * radius ^ 2)"""

from math import pi
def calc_area(option,*args):
    if option == 't':
        return 0.5 * args[0] * args[1]
    elif option == 'r':
        return args[0] * args[1]
    elif option == 'c':
        return round(pi * args[0] * args[0],2)
    else:
        return "invaild inputs"
    

print(f"The area of the triangle = {calc_area("t", 10 , 5)}")
print(f"The area of the rectangle = {calc_area("r", 10 , 5)}")
print(f"The area of the Circle = {calc_area("c", 5)}")
