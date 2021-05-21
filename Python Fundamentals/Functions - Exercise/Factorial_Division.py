def factorial_division(num1, num2):
    factorial1 = num1
    factorial2 = num2
    for num in range(num1-1, 0, -1):
        factorial1 *= num
    for num in range(num2-1, 0, -1):
        factorial2 *= num

    return factorial1 / factorial2


first_num = int(input())
second_num = int(input())

print(f"{factorial_division(first_num, second_num):.2f}")

