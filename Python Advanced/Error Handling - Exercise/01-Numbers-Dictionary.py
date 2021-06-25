numbers_dictionary = {}

while True:
    try:
        number_as_string = input()
        if number_as_string == "Search":
            break
        number = input()
        if number == "Search":
            break
        numbers_dictionary[number_as_string] = int(number)
    except ValueError:
        print("The variable must be an integer")
        continue

line = input()
while line != "Remove":
    searched = line
    print(numbers_dictionary.get(searched, "Number does not exist in dictionary"))
    line = input()

line = input()
while line != "End":
    searched = line
    try:
        del numbers_dictionary[searched]
    except KeyError:
        print("Number does not exist in dictionary")
        line = input()
        continue

    print(numbers_dictionary)
    line = input()

print(numbers_dictionary)
