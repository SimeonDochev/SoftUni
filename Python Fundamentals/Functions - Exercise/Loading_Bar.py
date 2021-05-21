def loading_bar(percentage):
    if percentage == 100:
        print("100% Complete!")
        print("[%%%%%%%%%%]")
    else:
        print(f"{percentage}% [", end="")
        for num in range(percentage//10):
            print("%", end="")
        for j in range(10 - percentage//10):
            print(".", end="")
        print("]")
        print("Still loading...")


number = int(input())
loading_bar(number)

