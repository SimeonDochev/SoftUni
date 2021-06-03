rows, cols = [int(num) for num in input().split()]

matrix = []

for row in range(rows):
    matrix.append([])
    for col in range(cols):
        palindrome = ''
        for i in range(3):
            if i == 0 or i == 2:
                palindrome += chr(row + 97)
            else:
                palindrome += chr(row + col + 97)
        matrix[row].append(palindrome)

for row in matrix:
    print(*row)
