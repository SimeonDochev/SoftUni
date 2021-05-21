def check_if_perfect(number):
    sum_of_divisors = 0
    for num in range(1, number):
        if number % num == 0:
            sum_of_divisors += num
    if sum_of_divisors == number:
        return True
    else:
        return False


number_from_console = int(input())

if check_if_perfect(number_from_console):
    print("We have a perfect number!")
else:
    print("It's not so perfect.")