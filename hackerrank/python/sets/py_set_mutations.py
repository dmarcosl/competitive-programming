input()
s = set(map(int, input().split()))

for _ in range(int(input())):
    method = input().split()[0]
    s2 = set(map(int, input().split()))

    if method == 'intersection_update':
        s.intersection_update(s2)
    elif method == 'update':
        s.update(s2)
    elif method == 'symmetric_difference_update':
        s.symmetric_difference_update(s2)
    elif method == 'difference_update':
        s.difference_update(s2)

print(sum(s))

