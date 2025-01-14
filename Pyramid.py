num = int(input("Enter the number"))

for i in range(1, num + 1):
    for j in range(1, i + 1):
        for k in range(1, num + 1 - j):
            print("*", end = " ")
    print()