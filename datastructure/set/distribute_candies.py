# 575 https://leetcode.com/problems/distribute-candies/
class Solution:
    """
    Runtime: 748 ms, faster than 99.38% of Python3 online submissions for Distribute Candies.
    Memory Usage: 16.2 MB, less than 65.95% of Python3 online submissions for Distribute Candies.
    """
    def distributeCandies(self, candyType: List[int]) -> int:
        return min(len(set(candyType)), len(candyType) // 2)