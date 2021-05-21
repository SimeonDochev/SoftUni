length = int(input())
width = int(input())
height = int(input())
percentage = float(input())

volume = (length * width * height) * 0.001
available_volume = volume * (1-percentage/100)
print(available_volume)
