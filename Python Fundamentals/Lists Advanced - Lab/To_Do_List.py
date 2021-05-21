def add_note(tasks, importance, task):
    tasks[importance-1] = task


to_do_list = [0] * 10
note = input()
while not note == "End":
    command_data = note.split("-")
    importance_value = int(command_data[0])
    task_info = command_data[1]
    add_note(to_do_list, importance_value, task_info)
    note = input()

final_to_do_list = [el for el in to_do_list if not el == 0]
print(final_to_do_list)
