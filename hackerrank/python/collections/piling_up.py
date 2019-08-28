for _ in range(int(input())):
    input()

    l = list(map(int, input().split()))
    lenght = len(l)
    i = 0

    while i < lenght - 1 and l[i] >= l[i+1]:
        i += 1

    while i < lenght - 1 and l[i] <= l[i+1]:
        i += 1

    print("Yes" if i == lenght - 1 else "No")

