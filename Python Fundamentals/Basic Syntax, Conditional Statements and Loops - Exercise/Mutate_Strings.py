starting_string = input()
end_string = input()

result = ""
previous_string = starting_string

for index in range(len(starting_string)):
    for i in range(index + 1):
        result += end_string[i]
    for i in range(index + 1, len(end_string)):
        result += starting_string[i]
    if not result == previous_string:
        print(result)
    previous_string = result
    result = ""
