"""
extend the example_check_html.py,
include more general case such as <body attribute1="xxx" attribute2="xxx">
"""
from example_stack import ArrayStack

def _match_function(raw):
    """function to check the match"""
    S = ArrayStack()
    j = raw.find('<')
    
    while j != -1:
        k = raw.find('>', j+1)
        if k == -1:     return False

        tag = raw[j+1:k]
        if tag[0] == '/':
            # this is a close tag
            if S.is_empty():             return False
            elif tag[1:] != S.top():    return False
            else:                       S.pop()
        
        else:
            # this is a starting tag
            space_index = tag.find(" ")
            if space_index == -1:
                S.push(tag)
            else:
                S.push(tag[:space_index])
        
        # finish this part, continue the loop
        j = raw.find("<", k+1)
    
    # the loop ends, the stack should be empty
    return S.is_empty()

def test_html_matched(filepath):
    file = open(filepath)
    lines = file.read()
    lines.replace("\n", " ")
    return _match_function(lines)


if __name__ == '__main__':

    print(test_html_matched("match_example1.html"))
    print(test_html_matched("match_example2.html"))
    print(test_html_matched("match_example3.html"))
    print(test_html_matched("not_match_example1.html"))
    print(test_html_matched("not_match_example2.html"))
            
"""
these example html does not contain <!DOCTYPE HTML>.
but it is very easy to include this toppest tag, 
simple delete this line during the reading file, if this line exists.
"""
