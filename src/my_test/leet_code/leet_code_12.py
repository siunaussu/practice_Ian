test_data = 2938

digit_list = []
loop_time = 0
while test_data != 0:
    res = test_data % 10
    digit_list.append(res * 10 ** loop_time)
    test_data = test_data // 10
    loop_time += 1

# print(digit_list)

def int_to_roman(num: int) -> str:
    M = ["", "M", "MM", "MMM"]
    C = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
    X = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
    I = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]

    return M[num//1000] + C[(num%1000)//100] + X[(num%100)//10] + I[num%10]

print(int_to_roman(46))
