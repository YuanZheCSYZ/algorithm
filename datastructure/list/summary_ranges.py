# 228 https://leetcode.com/problems/summary-ranges/

class Solution:
    """
    Runtime: 24 ms, faster than 95.70% of Python3 online submissions for Summary Ranges.
    Memory Usage: 14.2 MB, less than 50.76% of Python3 online submissions for Summary Ranges.
    """
    def summaryRanges(self, nums: list) -> list:
        results = []
        n = len(nums)

        starts = 0
        for index, x in enumerate(nums):
            if index + 1 < n:
                diff = nums[index + 1] - x
                if diff == 1:
                    continue
                else:
                    if starts < index:
                        results.append("{}->{}".format(nums[starts], nums[index]))
                    else:
                        results.append(str(x))

                    starts = index + 1
            else:
                if starts < index:
                    results.append("{}->{}".format(nums[starts], nums[index]))
                else:
                    results.append(str(x))

        return results


if __name__ == "__main__":
    assert ["0->2","4->5","7"] == Solution().summaryRanges([0,1,2,4,5,7])