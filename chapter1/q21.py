"""
record all stdin line by line until the EOFError,
then reverse print all lines
"""

lines = []
while True:
    try:
        input_line = input()
        lines.append(input_line)
    except EOFError:
        break

print()
print('\n'.join(reversed(lines)))