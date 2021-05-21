secret_message = input().split()

for word in secret_message:
    first_letter_ascii = ""
    for char in word:
        if char.isdigit():
            first_letter_ascii += char
    first_letter = chr(int(first_letter_ascii))
    word_letters = list(word[len(first_letter_ascii):])
    word_letters[0], word_letters[-1] = word_letters[-1], word_letters[0]
    deciphered_word = first_letter + "".join(word_letters)
    print(deciphered_word, end=" ")

