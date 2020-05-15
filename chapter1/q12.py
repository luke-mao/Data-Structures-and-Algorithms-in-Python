import random

def choice(data):
    return data[random.randrange(len(data))]


if __name__ == '__main__':
    data = [1,2,3,4,5,6,7,8,9,10]
    for i in range(5):
        print(choice(data))