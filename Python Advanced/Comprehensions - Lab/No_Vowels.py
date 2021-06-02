def is_not_vowel(char):
    if char.lower() not in "aeoui":
        return True
    return False


text = input()
print(''.join([char for char in text if is_not_vowel(char)]))
