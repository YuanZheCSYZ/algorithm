# 506 https://leetcode.com/problems/relative-ranks/

class Solution(object):
    """
    Runtime: 64 ms, faster than 66.94% of Python online submissions for Relative Ranks.
    Memory Usage: 14.7 MB, less than 18.15% of Python online submissions for Relative Ranks.
    """
    def findRelativeRanks(self, score):
        mapping = {
            0: "Gold Medal",
            1: "Silver Medal",
            2: "Bronze Medal"
        }
        sorted_s = sorted(enumerate(score), key=lambda x: -x[1])
        for i in range(len(sorted_s)):
            sorted_s[i] = (sorted_s[i][0], mapping[i] if i < 3 else str(i + 1))

        sorted_s.sort(key=lambda x: x[0])
        return map(lambda x: x[1], sorted_s)

    """
    Runtime: 68 ms, faster than 62.50% of Python online submissions for Relative Ranks.
    Memory Usage: 14.9 MB, less than 6.05% of Python online submissions for Relative Ranks.
    https://leetcode.com/problems/relative-ranks/discuss/98472/Python-solution
    """
    def findRelativeRanks(self, nums):
        sort = sorted(nums)[::-1]
        rank = ["Gold Medal", "Silver Medal", "Bronze Medal"] + map(str, range(4, len(nums) + 1))
        # !!! dict().get
        return map(dict(zip(sort, rank)).get, nums)
