num = int(input())

for i in range(num):
    for j in range(num):
        for k in range(num):
            print(f"{chr(97+i)}{chr(97+j)}{chr(97+k)}")
