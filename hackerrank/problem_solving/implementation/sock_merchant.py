import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    sock_dict = dict()
    for a in list(ar):
        sock_dict[a] = sock_dict.get(a, 0) + 1
    result = 0
    for key in sock_dict.keys():
        result += int(sock_dict[key] / 2)
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
