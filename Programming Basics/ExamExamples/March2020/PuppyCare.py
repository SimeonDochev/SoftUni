food_bought = int(input()) * 1000

food_eaten = 0
command = input()

while command != 'Adopted':
    food_eaten += int(command)
    command = input()

if food_eaten > food_bought:
    print(f'Food is not enough. You need {food_eaten - food_bought} grams more.')
else:
    print(f'Food is enough! Leftovers: {food_bought - food_eaten} grams.')
