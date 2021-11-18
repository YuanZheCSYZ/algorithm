# 2006 https://leetcode.com/problems/count-number-of-pairs-with-absolute-difference-k/submissions/

class Solution:
    """
    Runtime: 60 ms, faster than 93.61% of Python3 online submissions for Count Number of Pairs With Absolute Difference K.
    Memory Usage: 14.4 MB, less than 21.77% of Python3 online submissions for Count Number of Pairs With Absolute Difference K.
    """
    def countKDifference(self, nums: List[int], k: int) -> int:
        cnt = 0
        mapping = {}
        for num in nums:
            remaining = num - k
            if remaining in mapping:
                cnt += mapping[remaining]

            remaining = k + num
            if remaining in mapping:
                cnt += mapping[remaining]

            if num not in mapping:
                mapping[num] = 1
            else:
                mapping[num] += 1

        return cnt