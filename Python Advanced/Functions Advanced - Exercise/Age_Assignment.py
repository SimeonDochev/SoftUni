def age_assignment(*args, **kwargs):
    name_age_pairs = {}
    for name in args:
        for letter in kwargs.keys():
            if name[0] == letter:
                name_age_pairs[name] = kwargs[letter]
    return name_age_pairs


print(age_assignment("Peter", "George", G=26, P=19))
print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))