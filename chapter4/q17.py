# recursion, check palindrome

def palindrome(s, index=0):
    if index >= len(s)-index-1:
        return True
    else:
        if s[index] == s[len(s)-index-1]:
            index += 1
            return palindrome(s, index)
        else:
            return False


if __name__ == '__main__':
    word_list = ["cbc", "abba", "ab&^45", "racecar", "  today  if not"]

    for word in word_list:
        print("{}: {}".format(word, palindrome(word)))