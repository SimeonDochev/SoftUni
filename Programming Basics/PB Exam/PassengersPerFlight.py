from math import floor
companies_count = int(input())

most_passengers = 0
best_company = ''
average_passengers = 0
for i in range(companies_count):
    counter = 0
    passenger_count = 0
    company_name = input()
    command = input()
    while command != 'Finish':
        passenger_count += int(command)
        counter += 1
        command = input()
    passenger_count_average = floor(passenger_count / counter)
    if passenger_count_average > most_passengers:
        most_passengers = passenger_count_average
        best_company = company_name
        average_passengers = passenger_count_average
    print(f'{company_name}: {passenger_count_average:.0f} passengers.')

print(f'{best_company} has most passengers per flight: {average_passengers:.0f}')