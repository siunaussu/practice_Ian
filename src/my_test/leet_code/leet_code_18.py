"""
    leetCode_18
"""

def four_sum(nums: list[int], target: int) -> list[list[int]]:
    nums.sort()
    res = []
    for i in range(len(nums)-3):
        for j in range(i+1, len(nums)-3):
            left, right = j+1, len(nums)-1
            while left < right:
                total = nums[i] + nums[j] + nums[left] + nums[right]
                if total == target:
                    if [nums[i], nums[j], nums[left], nums[right]] not in res:
                        res.append([nums[i], nums[j], nums[left], nums[right]])
                    left += 1
                elif total < target:
                    left += 1
                else:
                    right -= 1

    return res
print(four_sum([1,0,-1,0,-2,2], 0))