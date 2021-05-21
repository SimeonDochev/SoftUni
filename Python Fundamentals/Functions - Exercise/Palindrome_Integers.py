def check_if_palindrome(numbers):
    result = []
    for number in numbers:
        if number == number[::-1]:
            result.append(True)
        else:
            result.append(False)
    for i in range(len(result)):
        print(result[i])


list_of_numbers = input().split(", ")

check_if_palindrome(list_of_numbers)
