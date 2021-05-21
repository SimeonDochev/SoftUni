def odd_and_even_sum(number):
    even_sum = 0
    odd_sum = 0

    for num in number:
        if int(num) % 2 == 0:
            even_sum += int(num)
        else:
            odd_sum += int(num)
    print(f"Odd sum = {odd_sum}, Even sum = {even_sum}")


number_as_string = input()

odd_and_even_sum(number_as_string)
