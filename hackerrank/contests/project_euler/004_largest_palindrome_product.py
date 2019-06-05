#!/bin/python3

def calculate_palindromes():
    palindrome_list = []
    for i in range(100, 1000):
        for j in range(100, 1000):
            product = i * j
            # Check if it's a palindrome
            if str(product) == str(product)[::-1] and product not in palindrome_list:
                palindrome_list.append(product)
    palindrome_list.sort()
    return palindrome_list


def find_largest_palindrome(palindrome_list, max_value):
    for i in range(len(palindrome_list) - 1, -1, -1):
        if palindrome_list[i] < max_value:
            return palindrome_list[i]


if __name__ == '__main__':
    palindrome_list = calculate_palindromes()
    for _ in range(int(input())):
        print(find_largest_palindrome(palindrome_list, int(input())))

