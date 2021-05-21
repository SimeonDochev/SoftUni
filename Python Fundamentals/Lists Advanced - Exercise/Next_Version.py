version_as_string = input().split(".")
version = [int(el) for el in version_as_string]

for num in range(len(version) - 1, -1, -1):
    if version[num] < 9:
        version[num] += 1
        break
    if version[num] == 9:
        version[num] = 0
        if not version[num-1] == 9:
            version[num-1] += 1
            break
        else:
            version[num-1] = 0
            version[num-2] += 1
            break

next_version = list(map(str, version))
print(".".join(next_version))


