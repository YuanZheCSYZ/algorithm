# 219 https://leetcode.com/problems/contains-duplicate-ii/submissions/

class Solution:
    """
    Runtime: 884 ms, faster than 13.82% of Python3 online submissions for Contains Duplicate II.
    Memory Usage: 36.1 MB, less than 5.03% of Python3 online submissions for Contains Duplicate II.
    """
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        sorted_nums = sorted(enumerate(nums), key=lambda x: (x[1], x[0]))
        length = len(sorted_nums)
        for x in range(length - 1):
            if sorted_nums[x][1] == sorted_nums[x + 1][1] and sorted_nums[x + 1][0] - sorted_nums[x][0] <= k:
                return True

        return False

    """
    Runtime: 568 ms, faster than 99.37% of Python3 online submissions for Contains Duplicate II.
    Memory Usage: 27.7 MB, less than 52.15% of Python3 online submissions for Contains Duplicate II.
    """
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        mapping = {}
        for index, x in enumerate(nums):
            if x in mapping:
                if index - mapping[x] <= k:
                    return True
                else:
                    mapping[x] = index
            else:
                mapping[x] = index

        return False