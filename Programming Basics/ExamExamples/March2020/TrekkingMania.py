groups_count = int(input())

total_people = 0
musala_count = 0
monblan_count = 0
kilimandjaro_count = 0
k2_count = 0
everest_count = 0

for i in range(groups_count):
    people = int(input())
    total_people += people
    if people <= 5:
        musala_count += people
    elif 6 <= people <= 12:
        monblan_count += people
    elif 13 <= people <= 25:
        kilimandjaro_count += people
    elif 26 <= people <= 40:
        k2_count += people
    elif people >= 41:
        everest_count += people

print(f'{musala_count / total_people * 100:.2f}%')
print(f'{monblan_count / total_people * 100:.2f}%')
print(f'{kilimandjaro_count / total_people * 100:.2f}%')
print(f'{k2_count / total_people * 100:.2f}%')
print(f'{everest_count / total_people * 100:.2f}%')
