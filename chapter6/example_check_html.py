"""
textbook example, check html pages
"""

from example_stack import ArrayStack

def match_function(raw):
    """return True if all tags are matched"""
    S = ArrayStack()    # infinite length stack
    j = raw.find('<')   # string.find, return -1 if not found, return the index if found

    while j != -1:      # while still has <
        k = raw.find('>', j+1)  # from index >= j+1 find >
        if k == -1:     return False    # if not found, the bracket does not match

        tag = raw[j+1:k]    # does not include < and >
        if tag[0] == '/':   # the close tag
            if S.is_empty():            return False 
            elif tag[1:] != S.top():    return False
            else:                       S.pop()

        else:
            S.push(tag)     # push the whole tag into it, since it does not have / sign
        
        # continue the loop, find next j >= k+1
        j = raw.find('<', k+1)  
    
    return S.is_empty()     # finish the loop, if stack is empty, the html page matches


def test_html_matched(filepath):
    file = open(filepath)
    lines = file.read()
    lines.replace("\n", " ")
    return match_function(lines)


if __name__ == '__main__':

    print(test_html_matched("match_example1.html"))
    print(test_html_matched("not_match_example1.html"))
