favourite_book = input()
current_book = input()
count = 0

while current_book != 'No More Books':
    count += 1
    if current_book == favourite_book:
        print(f'You checked {count-1} books and found it.')
        break
    current_book = input()

if current_book == 'No More Books':
    print('The book you search is not here!')
    print(f'You checked {count} books.')
