waiting_people = int(input())
wagons_list = list(map(int, input().split()))

for wagon in range(len(wagons_list)):
    if waiting_people == 0:
        break
    while wagons_list[wagon] < 4 and waiting_people >= 1:
        wagons_list[wagon] += 1
        waiting_people -= 1

if waiting_people == 0 and not wagons_list.count(4) == len(wagons_list):
    print(f"The lift has empty spots!\n{' '.join(list(map(str, wagons_list)))}")
elif waiting_people > 0:
    print(f"There isn't enough space! {waiting_people} people in a queue!\n{' '.join(list(map(str, wagons_list)))}")
elif waiting_people == 0 and wagons_list.count(4) == len(wagons_list):
    print(" ".join(list(map(str, wagons_list))))
