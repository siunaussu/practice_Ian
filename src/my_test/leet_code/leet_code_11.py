def most_water(arg: list[int]) -> int:
    if len(arg) < 2:
        return 0

    max_res = 0
    for i in range(0, len(arg)):
        for j in range(i, len(arg)):
            min_height = min(arg[i], arg[j])
            if (j - i) * min_height > max_res:
                max_res = (j - i) * min_height
    return max_res

def max_Area(height: list[int]) -> int:
    max_area = 0
    left = 0
    right = len(height) - 1

    while left < right:
        max_area = max(max_area, (right - left) * min(height[left], height[right]))

        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return max_area


heights = [1,8,6,2,5,4,1,110,7]

# a = most_water(heights)
a = max_Area(heights)
print(a)
