class EncryptionGenerator:
    def __init__(self, text: str):
        self.text = text

    def __add__(self, other):
        if not isinstance(other, int):
            raise ValueError("You must add a number.")

        result = ''
        for char in self.text:
            ascii_num = ord(char)
            ascii_num += other
            while ascii_num < 32:
                ascii_num += 95
            while ascii_num > 126:
                ascii_num -= 95

            result += chr(ascii_num)

        return result


example = EncryptionGenerator('Super-Secret Message')
print(example + 20)
print(example + (-52))

