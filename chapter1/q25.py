"""
input a sentence, return the sentence without punctuation
use isalnum(): Returns True if all characters in the string are alphanumeric.
also use isspace: since the whitespace should be retained, only punctuation are removed
"""

def no_punctuation(s):
    if (not isinstance(s, str)):
        raise ValueError("Input must be a string")

    if len(s) == 0:
        return ""
    
    result = ""
    for i in range(len(s)):
        if s[i].isalnum() or s[i].isspace():
            result += s[i]
    
    return result


if __name__ == '__main__':
    print("{} => {}".format("Let's try, Mike", no_punctuation("Let's try, Mike")))
    print("{} => {}".format("Let,,,,,!!!! Mike", no_punctuation("Let,,,,,!!!! Mike")))
    print("{} => {}".format(",,,,,,,,,,", no_punctuation(",,,,,,,,,,")))
    # print("{} => {}".format(5, no_punctuation(5)))



