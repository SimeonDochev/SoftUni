class sequence_repeat:
    def __init__(self, sequence, number):
        self.sequence = sequence
        self.number = number
        self.curr_idx = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.number == 0:
            raise StopIteration
        curr_char = self.sequence[self.curr_idx]
        self.curr_idx += 1
        if self.curr_idx == len(self.sequence):
            self.curr_idx = 0
        self.number -= 1
        return curr_char


result = sequence_repeat('abc', 5)
for item in result:
    print(item, end='')
