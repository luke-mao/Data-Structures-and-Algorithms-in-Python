"""
write the reverse function
"""
def my_reverse(data):
    data2 = data[:]     # or data2 = list(data)
    for i in range(0, len(data2)//2):
        agent = data2[i]
        data2[i] = data2[len(data2)-i-1]
        data2[len(data2)-i-1] = agent
    
    return data2


if __name__ == '__main__':
    data1 = [1,4,9,7,10]
    data2 = [5,8,10,-10]

    print("Origin: {}, reverse:{}".format(data1, my_reverse(data1)))
    print("Origin: {}, reverse:{}".format(data2, my_reverse(data2)))

    # print(data1)  # use to check whether the input variables are changed 
