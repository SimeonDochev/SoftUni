import math
figure_type = input()

if figure_type == 'square':
    side = float(input())
    square_area = math.pow(side, 2)
    print(f'{square_area:.3f}')
elif figure_type == 'rectangle':
    first_side = float(input())
    second_side = float(input())
    rectangle_area = first_side * second_side
    print(f'{rectangle_area:.3f}')
elif figure_type == 'circle':
    radius = float(input())
    circle_area = math.pi * math.pow(radius, 2)
    print(f'{circle_area:.3f}')
elif figure_type == 'triangle':
    side = float(input())
    height = float(input())
    triangle_area = side * height / 2
    print(f'{triangle_area:.3f}')

