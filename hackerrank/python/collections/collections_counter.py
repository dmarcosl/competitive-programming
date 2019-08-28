input()
sizes = list(map(int, input().split()))

total = 0

for _ in range(int(input())):
    size, value = list(map(int, input().split()))
    if size in sizes:
        total += value
        sizes.remove(size)

print(total)

