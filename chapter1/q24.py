"""
write a function, calculate the number of a e i o u in the letter
"""

def count_vowel(s):
    if not isinstance(s, str):
        raise ValueError("ValueError: input must be a string")
    
    if len(s) == 0:
        return 0

    counter = 0
    vowel_list = ['a', 'e', 'i', 'o', 'u']

    for letter in s:
        if letter.lower() in vowel_list: counter += 1
    
    return counter


if __name__ == '__main__':
    print("{}: {}".format("aeiouAEIOU", count_vowel("aeiouAEIOU")))
    # print("{}: {}".format(5, count_vowel(5)))
    print("{}: {}".format("", count_vowel("")))
    print("{}: {}".format("batch", count_vowel("batch")))
