"""
recursion, sum the two dimensional list
"""

def sum_one_list(data):
    total = 0
    if not isinstance(data, list):
        return data     # for one value, just return the value for the addtion in total += sum_one_list(element)
    else:               # for a list, go deeper into each element
        for element in data:
            total += sum_one_list(element)
        return total

if __name__ == '__main__':
    data = [[1,2,3], [4,5,6], [7,8],[9], [10]]
    print(sum_one_list(data))