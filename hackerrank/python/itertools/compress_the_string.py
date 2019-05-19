from itertools import groupby

for key, group in groupby(list(map(int, list(input())))):
    print('({}, {})'.format(len(list(group)), key), end=' ')
