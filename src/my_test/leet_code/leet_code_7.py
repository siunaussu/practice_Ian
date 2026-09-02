def reverse(x: int) -> int:
    INT_MIN, INT_MAX = -2 ** 31, 2 ** 31 - 1

    sign = -1 if x < 0 else 1
    x = abs(x)

    result = 0
    while x != 0:
        digit = x % 10
        x //= 10

        # Check BEFORE updating result, to avoid ever exceeding the range
        if result > (INT_MAX - digit) // 10:
            return 0

        result = result * 10 + digit

    return sign * result

print(reverse(-8463847412))
