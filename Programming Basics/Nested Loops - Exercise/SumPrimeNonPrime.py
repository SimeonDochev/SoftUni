prime_num_sum = 0
non_prime_num_sum = 0

command = input()
while command != 'stop':
    number = int(command)
    if number < 0:
        print('Number is negative.')
        command = input()
        continue
    counter = 0
    for i in range(1, number + 1):
        if number % i == 0:
            counter += 1

    if counter == 2:
        prime_num_sum += number
    else:
        non_prime_num_sum += number
    command = input()

print(f'Sum of all prime numbers is: {prime_num_sum}')
print(f'Sum of all non prime numbers is: {non_prime_num_sum}')
