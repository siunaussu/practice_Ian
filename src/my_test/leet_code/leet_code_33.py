def bad_search(nums: list[int], target: int) -> int:
    if target in nums:
        return nums.index(target)
    else:
        return -1


def good_search(nums: list[int], target: int) -> int:
    left, right = 0, len(nums) - 1
    i = 0
    while left <= right:
        i += 1
        mid = (left + right) // 2

        if nums[mid] == target:
            print(f"loop {i} times!")
            return mid

        if nums[left] <= nums[mid]:
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1
    print(f"loop {i} times!")
    return -1


a = [1, 2, 3, 5, 6, 7, 0]
print(good_search(a, 6))

