import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    jumps = 0
    skip = False
    for idx in range(len(c)):
        if idx == len(c):
            print('break', idx)
            break
        elif skip or idx == 0:
            skip = False
            continue
        elif c[idx] == 1 or (idx + 1 <= len(c) - 1 and c[idx + 1] == 0):
            skip = True
            print('skip')
        else:
            print('not skip')
        jumps += 1
    return jumps

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
