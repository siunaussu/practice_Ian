class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s

        def expand(left: int, right: int) -> tuple[int, int]:
            """从left,right向外扩散，返回回文的左右边界 l,r"""
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            # 退出循环时，left、right已经越界/不等，回文有效区间是 [left+1, right‑1]
            return left + 1, right - 1

        start, end = 0, 0
        for i in range(len(s)):
            # 奇数回文：中心i
            l1, r1 = expand(i, i)
            # 偶数回文：中心 i,i+1
            l2, r2 = expand(i, i + 1)

            # 比较两个回文长度，保留更长的
            if r1 - l1 > end - start:
                start, end = l1, r1
            if r2 - l2 > end - start:
                start, end = l2, r2

        # 切片左闭右开，end要+1
        return s[start: end + 1]

result = Solution().longestPalindrome("12")
print(result)