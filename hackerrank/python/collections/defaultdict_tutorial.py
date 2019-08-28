from collections import defaultdict

n, m = list(map(int, input().split()))

d = defaultdict(list)
[d[input()].append(str(i)) for i in range(1, n + 1)]

[print(' '.join(d[input()]) or -1) for _ in range(m)]

