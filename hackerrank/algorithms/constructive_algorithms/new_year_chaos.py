#!/bin/python3

# Complete the minimumBribes function below.
def minimumBribes(line_places):
    changes = 0
    for i in range(len(line_places))[::-1]:
        if line_places[i] - (i + 1) > 2:
            return 'Too chaotic'
        for j in range(max(0, line_places[i] - 2), i):
            if line_places[j] > line_places[i]:
                changes += 1
    return changes

if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        print(minimumBribes(q))

