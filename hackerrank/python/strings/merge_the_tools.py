def merge_the_tools(string, k):
    while string:
        substring = string[0:k]
        seen = ''
        for char in substring:
            if char not in seen:
                seen += char
        print(seen)
        string = string[k:]

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)

