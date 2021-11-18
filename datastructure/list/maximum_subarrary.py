# 53 https://leetcode.com/problems/maximum-subarray/submissions/

class Solution:
    """
    Runtime: 672 ms, faster than 86.39% of Python3 online submissions for Maximum Subarray.
    Memory Usage: 28.8 MB, less than 9.80% of Python3 online submissions for Maximum Subarray.
    """
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) <= 0:
            return None

        result = nums[0]
        tmp_result = result
        for x in range(1, len(nums)):
            num = nums[x]
            if tmp_result < 0:
                tmp_result = 0
            tmp_result += num
            if result < tmp_result:
                result = tmp_result

        return result

    """
    Runtime: 648 ms, faster than 89.98% of Python3 online submissions for Maximum Subarray.
    Memory Usage: 28.7 MB, less than 30.21% of Python3 online submissions for Maximum Subarray.
    """
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) <= 0:
            return None

        result = nums[0]
        tmp_result = result
        for x in range(1, len(nums)):
            num = nums[x]
            if tmp_result < 0:
                tmp_result = 0
            tmp_result += num
            if result < tmp_result:
                result = tmp_result

        return result