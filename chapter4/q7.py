# recursion, convert a string to integer
def convert(s):
    """O(n) in time and space"""
    if len(s) == 1:
        return int(s)
    else:
        return int(s[0]) * (10 ** (len(s)-1)) + convert(s[1:])


if __name__ == '__main__':
    print(convert("135312"))