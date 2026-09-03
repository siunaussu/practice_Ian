def search_range(nums: list[int], target: int) -> list[int]:
    def find_bound(is_first: bool) -> int:
        lo, hi = 0, len(nums) - 1
        result = -1
        while lo <= hi:
            mid = (lo + hi) // 2
            if nums[mid] == target:
                result = mid
                if is_first:
                    hi = mid - 1  # keep searching left
                else:
                    lo = mid + 1  # keep searching right
            elif nums[mid] < target:
                lo = mid + 1
            else:
                hi = mid - 1
        return result

    first = find_bound(is_first=True)
    if first == -1:
        return [-1, -1]
    last = find_bound(is_first=False)
    return [first, last]


a = [5,7,7,7,8,8,10]
print(search_range(a,7))