# def divide(dividend: int, divisor: int) -> int:
#     flag = False
#     if (dividend > 0 and divisor > 0) or (dividend < 0 and divisor < 0):
#         flag = True
#
#     def minus(number_wait_minus: int, number_minus: int, count: int=0) -> int:
#         if number_wait_minus < number_minus:
#             return count
#         number_wait_minus -= number_minus
#         count += 1
#         res = minus(number_wait_minus, number_minus, count)
#         return res
#
#     return minus(abs(dividend), abs(divisor)) if flag else 0 - minus(abs(dividend), abs(divisor))

def divide(dividend: int, divisor: int) -> int:
    if divisor == 0:
        return ZeroDivisionError("divisor cannot be zero")

    sign = (dividend < 0) != (divisor < 0)
    dividend, divisor = abs(dividend), abs(divisor)

    quotient = 0
    while dividend >= divisor:
        temp, multiple = divisor, 1
        while (temp << 1) <= dividend:
            temp <<= 1
            multiple <<= 1
        dividend -= temp
        quotient += multiple

    return quotient if not sign else -quotient

print(divide(-2147483648, 0))

