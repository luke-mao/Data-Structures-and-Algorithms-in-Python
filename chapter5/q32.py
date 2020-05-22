"""
a[i][j][k] + b[i][j][k]
"""

def addition(a, b):
    result = [[None]*3 for _ in range(3)]
    
    for row in range(len(a)):
        for col in range(len(a[row])):
            result[row][col] = a[row][col] + b[row][col] 
    
    return result



if __name__ == '__main__':
    
    a = [[1,2,3],[4,5,6],[7,8,9]]
    b = a[:]

    print(addition(a,b))
        