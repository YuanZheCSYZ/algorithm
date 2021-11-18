# 1 https://leetcode.com/problems/two-sum/submissions/

class Solution0:
    """
    Runtime: 3236 ms, faster than 29.95% of Python3 online submissions for Two Sum.
    Memory Usage: 14.8 MB, less than 92.42% of Python3 online submissions for Two Sum.
    O(N^2)
    """
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for index1, num1 in enumerate(nums):
            for index2 in range(index1 + 1, len(nums)):
                if target == num1 + nums[index2]:
                    return [index1, index2]

        return []

class Solution1:
    """
    Runtime: 68 ms, faster than 57.94% of Python3 online submissions for Two Sum.
    Memory Usage: 16.1 MB, less than 8.84% of Python3 online submissions for Two Sum.
    O(N x log(N))
    """
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sorted_nums = sorted([(x, index) for index, x in enumerate(nums)], key=lambda x: -x[0])
        for index, num_1 in enumerate(sorted_nums):
            remain = target - num_1[0]
            if remain < sorted_nums[-1][0]:
                continue

            num_2 = self.bi_search(index + 1, len(sorted_nums), remain, sorted_nums)
            if num_2:
                return [num_1[1], num_2[1]]

        return []

    def bi_search(self, index_from, index_to, target, nums):
        if index_to < index_from:
            return None

        pivot_index = (index_from + index_to) // 2
        if target < nums[pivot_index][0]:
            return self.bi_search(pivot_index + 1, index_to, target, nums)
        elif target == nums[pivot_index][0]:
            return nums[pivot_index]
        else:
            return self.bi_search(index_from, pivot_index - 1, target, nums)


class Solution2:
    """
    Runtime: 56 ms, faster than 90.92% of Python3 online submissions for Two Sum.
    Memory Usage: 15.5 MB, less than 19.55% of Python3 online submissions for Two Sum.
    N
    """
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapping = {num: index for index, num in enumerate(nums)}
        for index, num in enumerate(nums):
            remain = target - num
            if remain in mapping and mapping[remain] != index:
                return [index, mapping[remain]]

        return []

class Solution2:
    """
    Runtime: 60 ms, faster than 79.50% of Python3 online submissions for Two Sum.
    Memory Usage: 15.1 MB, less than 60.42% of Python3 online submissions for Two Sum.
    """
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h = {}
        for i, num in enumerate(nums):
            n = target - num
            if n not in h:
                h[num] = i
            else:
                return [h[n], i]