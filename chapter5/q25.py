"""
accomplish the function remove_all(data, value),
the time complexity is O(n)
"""

def remove_all(data, value):
    
    index_list = [None]*len(data)
    index_num = 0

    for i in range(len(data)):
        if data[i] == value:
            index_list[index_num] = i
            index_num += 1
    
    if index_num == 0:
        raise ValueError("Value {} is not in the data".format(value))
    else:
        # remove all values in place
        result = [None]*(len(data)-index_num)   # construct the result list, fix the length
        result_i = 0
        data_i = 0
        for i in range(index_num):
            
            remove_index = index_list[i]    # this index should not be copied

            result[result_i:remove_index-i] = data[data_i:remove_index] # caution about the index range
            result_i = remove_index - i     # minus i
            data_i = remove_index + 1

        result[result_i:]   = data[data_i:]

        return result   # in-place deletion


def remove_all2(data, value):
    """use the solution from the solution manual, more easier to understand and learn"""
    keep = 0
    for i in range(len(data)):
        if data[i] != value:
            data[keep] = data[i]        # modify the result in place
            keep += 1
    
    data[keep:] = []


if __name__ == '__main__':
    
    data = [1,2,3,4,5,5,5,6,7,8,8,9,10]
    print(data)

    remove_all2(data, 5)
    print(data)

    remove_all2(data, 4)
    print(data)

    remove_all2(data, 8)
    print(data)

    # data = remove_all(data, 20)   # value not in the list, raise ValueError

