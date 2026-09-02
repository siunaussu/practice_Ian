"""
    leetCode6
    zigzag
"""


def convert(s: str, num_rows: int) -> str:
    if num_rows == 1 or num_rows >= len(s):
        return s

    idx, d = 0, 1
    rows = [[] for _ in range(num_rows)]

    for char in s:
        rows[idx].append(char)
        if idx == 0:
            d = 1
        elif idx == num_rows - 1:
            d = -1
        idx += d

    for i in range(num_rows):
        rows[i] = ''.join(rows[i])

    return ''.join(rows)


a = 'abcdefghik'
print(convert(a, 3))
