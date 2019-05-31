#!/bin/python3

for _ in range(int(input().strip())):
    n = int(input().strip())

    # Total of multiples of 3, 5 and the product of both
    n3  = (n - 1) // 3
    n5  = (n - 1) // 5
    n15  = (n - 1) // 15

    # Sum of n multiples of any number is that number multiply by (half of multiplication of n and n+1)
    sum_n3 = 3 * (n3 * (n3 + 1)) // 2
    sum_n5 = 5 * (n5 * (n5 + 1)) // 2
    sum_n15 = 15 * (n15 * (n15 + 1)) // 2

    print(sum_n3 + sum_n5 - sum_n15)

