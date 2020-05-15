"""
give an example of index error, and print the specific sentence
"""
try:
    a = [1,2,3]
    a[len(a)] = 4
except IndexError:
    print("Don't try buffer overflow attacks in Python!")


