from math import floor
length = float(input()) * 100
width = float(input()) * 100 - 100

seats_row = floor(width / 70)
rows = floor(length / 120)

print(rows * seats_row - 3)









