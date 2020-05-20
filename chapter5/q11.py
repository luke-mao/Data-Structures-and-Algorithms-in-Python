"""
use basic control structure to calculate the sum of values in n*n array
"""

n = 20
data = [[1]*n for _ in range(n)]

total = 0
for i in range(len(data)):
    for j in range(len(data[i])):
        total += data[i][j]

print(total)