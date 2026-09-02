def three_sum_closest(arr: list[int], target: int) -> int:
    arr.sort()
    res = arr[0] + arr[1] + arr[2]

    for i in range(len(arr) - 2):
        left = i + 1
        right = len(arr) - 1

        while left < right:
            total = arr[i] + arr[left] + arr[right]
            if abs(total - target) < abs(res - target):
                res = total

            if total == target:
                return res
            if total < target:
                left += 1
            else:
                right -= 1

    return res

a = [-1, 0, 1, 2, 1, -4]

print(three_sum_closest(a, 5))
