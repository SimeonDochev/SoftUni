def characters_in_range_ascii(char1, char2):
    for char in range(ord(char1) + 1, ord(char2)):
        print(chr(char), end=" ")


first_char = input()
second_char = input()

characters_in_range_ascii(first_char, second_char)
