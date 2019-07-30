n, m = [int(i) for i in input().split()]

for i in range(n):
    if i == int(n / 2):
        print('{0}WELCOME{0}'.format('-' * int((m - 7) / 2)))

    elif i < int(n / 2):
        dots = i + i + 1
        print('{0}{1}{0}'.format('-' * int((m - (dots * 3)) / 2), '.|.' * dots))

    elif i > int(n / 2):
        j = int(n / 2) - (i - int(n / 2))
        dots = j + j + 1
        print('{0}{1}{0}'.format('-' * int((m - (dots * 3)) / 2), '.|.' * dots))

