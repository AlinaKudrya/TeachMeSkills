from classes_12 import *

center_of_circle = Point(2,5)
circle = Circle(center_of_circle, 5)
print(f'The perimeter of the circle = {circle.perimeter()}\n'
      f'The area of the circle = {circle.area()}\n')

first_point = Point(1,1)
second_point = Point(2,4)
third_point = Point(4,2)
triangle = Triangle(first_point,second_point,third_point)
print(f'The perimeter of the triangle = {triangle.perimeter()}\n'
      f'The area of the triangle = {triangle.area()}\n')

first_point = Point(1,1)
second_point = Point(2,4)
square = Square(first_point,second_point)
print(f'The perimeter of the square = {square.perimeter()}\n'
      f'The area of the square = {square.area()}\n')