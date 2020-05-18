"""
reverse print a string
"""

# import s is a list
# use list(s) to avoid the problem: str object does not support item assignment 
def reverse(s, left_i, right_i):
    if left_i > right_i:
        return s
    else:
        # list support item assignment
        list_s = list(s)
        list_s[left_i], list_s[right_i] = list_s[right_i], list_s[left_i]

        return reverse("".join(list_s), left_i+1, right_i-1)


if __name__ == '__main__':

    word = ["abc", "pots&pans", "today is beautiful"]
    for each in word:
        print(reverse(each, 0, len(each)-1))    # the list(str) has same length as the string