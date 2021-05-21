electrons_count = int(input())

atom_shells_list = []
shell_number = 1

while electrons_count > 0:
    current_shell_electrons = 2 * shell_number ** 2
    if current_shell_electrons > electrons_count:
        atom_shells_list.append(electrons_count)
    else:
        atom_shells_list.append(current_shell_electrons)
    electrons_count -= current_shell_electrons
    shell_number += 1

print(atom_shells_list)
