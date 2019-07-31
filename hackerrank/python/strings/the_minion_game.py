def minion_game(string):
    # your code goes here
    vowels = frozenset("AEIOU")
    size = len(string)
    s = k = 0
    for i, sub in enumerate(string):
        if sub in 'AEIOU':
            k += size - i
        else:
            s += size - i
    if s > k:
        print('Stuart {}'.format(s))
    elif k > s:
        print('Kevin {}'.format(k))
    else:
        print('Draw')


if __name__ == '__main__':
    s = input()
    minion_game(s)

