# 645 https://leetcode.com/problems/set-mismatch/

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        """
        Runtime: 236 ms, faster than 35.45% of Python3 online submissions for Set Mismatch.
        Memory Usage: 15.3 MB, less than 94.57% of Python3 online submissions for Set Mismatch.
        """
        i = 0
        d = None
        while True:
            x = nums[i]
            if i + 1 == x:
                i += 1
            else:
                if nums[x - 1] == x:
                    d = x
                    break
                else:
                    nums[i], nums[x - 1] = nums[x - 1], x

        return [d, (1 + len(nums)) * len(nums) // 2 - sum(nums) + d]

    def findErrorNums(self, nums: List[int]) -> List[int]:
        """
        Runtime: 192 ms, faster than 80.17% of Python3 online submissions for Set Mismatch.
        Memory Usage: 16 MB, less than 37.71% of Python3 online submissions for Set Mismatch.
        """
        return [sum(nums) - sum(set(nums)), sum(range(1, len(nums)+1)) - sum(set(nums))]

    def findErrorNums(self, nums: List[int]) -> List[int]:
        """
        Runtime: 184 ms, faster than 91.78% of Python3 online submissions for Set Mismatch.
        Memory Usage: 16.1 MB, less than 27.53% of Python3 online submissions for Set Mismatch.
        """
        n = len(nums)
        s = sum(set(nums))
        return [sum(nums) - s, (1 + n) * n // 2 - s]
