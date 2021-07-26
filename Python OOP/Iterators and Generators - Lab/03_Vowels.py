class vowels:
    _VOWELS = "AEYUOI"

    def __init__(self, text):
        self.text = text
        self.start_idx = 0
        self.vowels_list = [char for char in self.text if char.upper() in vowels._VOWELS]
        self.end_idx = len(self.vowels_list) - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.start_idx > self.end_idx:
            raise StopIteration
        current_char = self.vowels_list[self.start_idx]
        self.start_idx += 1
        return current_char


my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)
