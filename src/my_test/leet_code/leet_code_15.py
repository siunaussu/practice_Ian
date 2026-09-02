from collections import defaultdict

a = [-1,0,1,2,-1,-4]


# def triplets(arg: list[int]) -> list[list[int]]:
#     res = []
#     for i in range(len(arg)):
#         for j in range(i+1, len(arg)):
#             for k in range(j+1, len(arg)):
#                 if arg[i] + arg[j] + arg[k] == 0:
#                     flag = False
#                     for sub_arg in res:
#                         if arg[i] in sub_arg and arg[j] in sub_arg and arg[k] in sub_arg:
#                             flag = True
#                             break
#                     if not flag:
#                         res.append([arg[i], arg[j], arg[k]])
#
#
#     return res
#
# print(triplets(a))


def three_sum(nums: list[int]) -> list[list[int]]:
    neg = defaultdict(int)
    pos = defaultdict(int)
    zeros = 0

    for x in nums:
        if x < 0:
            neg[x] += 1
        elif x > 0:
            pos[x] += 1
        else:
            zeros += 1

    r = []

    if zeros:
        for n in neg:
            if -n in pos:
                r.append((0, n, -n))

        if zeros > 2:
            r.append((0, 0, 0))

    for set_a, set_b in ((neg, pos), (pos, neg)):
        set_a_items = list(set_a.items())
        for i, (x, q) in enumerate(set_a_items):
            for x2, q2 in set_a_items[i:]:
                if x != x2 or (x == x2 and q > 1):
                    if -x - x2 in set_b:
                        r.append((x, x2, -x - x2))

    return r

three_sum(a)
