# determine if vowell and consonants
# similar: count the level of a tree

vowel = ['a', 'e', 'i', 'o', 'u']

def count(s):
    if s[0] in vowel:   a = 1
    else:               a = -1
    
    if len(s) == 1: return a
    else:           return a + count(s[1:])

def check(s):
    a = count(s)
    
    if a > 0:       print("{}: {} more vowels".format(s, a))
    elif a == 0:    print("{}: equal number of vowel and consonant".format(s))
    else:           print("{}: {} more consonants".format(s, -a))


if __name__ == '__main__':
    check("string")
    check("aba")
    check("aabb")
    