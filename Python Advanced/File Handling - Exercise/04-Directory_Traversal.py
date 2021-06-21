import os

file_extensions = {}

_, _, files = next(os.walk(input()))

for file in files:
    ext = file.split('.')[-1]
    if ext not in file_extensions:
        file_extensions[ext] = []
    file_extensions[ext].append(file)

with open(os.path.expanduser('~/Desktop/report.txt'), 'w') as f:
    for ext, files in sorted(file_extensions.items()):
        f.write(f".{ext}\n")
        for file in sorted(files):
            f.write(f"---{file}\n")
