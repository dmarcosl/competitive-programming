from collections import Counter, defaultdict

occurrences = Counter(input())

d = defaultdict(list)
[d[occurrence[1]].append(occurrence[0]) for occurrence in occurrences.items()]

c = 0
for number in sorted(d.keys(), reverse=True):
    d[number].sort()
    for char in d[number]:
        if c == 3:
            break
        c += 1
        print('{} {}'.format(char, number))

