height = float(input())
length = float(input())
triangle_height = float(input())

side1 = height * height - 1.2 * 2
side2 = height * length - 1.5 * 1.5
side_area = (side2 * 2) + side1 + (height * height)
roof1 = height * length
roof2 = height * triangle_height / 2
roof_area = 2 * roof1 + 2 * roof2

green_paint = side_area / 3.4
red_paint = roof_area / 4.3

print(f'{green_paint:.2f}')
print(f'{red_paint:.2f}')
