"""
similar to q11, but more simplier
"""

n = 20
data = [[1]*n for _ in range(n)]

total = sum(sum(sub_list) for sub_list in data)

print(total)