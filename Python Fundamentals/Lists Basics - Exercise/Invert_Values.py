values = input()

values_as_list = values.split()
result = []
for num in range(len(values_as_list)):
    inverted_value = int(values_as_list[num]) * -1
    result.append(inverted_value)

print(result)
