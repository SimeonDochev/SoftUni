def calculate(oper, num1, num2):
    if oper == "multiply":
        return num1 * num2
    elif oper == "divide":
        return num1 // num2
    elif oper == "add":
        return num1 + num2
    elif oper == "subtract":
        return num1 - num2


operator = input()
first_num = int(input())
second_num = int(input())

print(calculate(operator, first_num, second_num))
