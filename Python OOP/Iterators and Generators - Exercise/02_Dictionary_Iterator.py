class dictionary_iter:
    def __init__(self, dictionary):
        self.dictionary = dictionary
        self.start = 0
        self.end = len(dictionary) - 1
        self.keys = list(dictionary.keys())

    def __iter__(self):
        return self

    def __next__(self):
        if self.start > self.end:
            raise StopIteration
        curr_key = self.keys[self.start]
        self.start += 1
        return curr_key, self.dictionary[curr_key]


result = dictionary_iter({1: "1", 2: "2"})
for x in result:
    print(x)
