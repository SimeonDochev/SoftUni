database = {}

command = input()
while not command == "End":
    company, emp_id = command.split(" -> ")
    if company not in database:
        database[company] = [emp_id]
    elif emp_id in database[company]:
        command = input()
        continue
    else:
        database[company].append(emp_id)
    command = input()

for comp, emp in sorted(database.items(), key=lambda k: k[0]):
    print(comp)
    for i in range(len(database[comp])):
        print(f"-- {database[comp][i]}")
