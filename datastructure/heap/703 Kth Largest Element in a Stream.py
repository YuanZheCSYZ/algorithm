# https://leetcode.com/problems/kth-largest-element-in-a-stream/

"""
Runtime: 564 ms, faster than 13.66% of Python3 online submissions for Kth Largest Element in a Stream.
Memory Usage: 18.5 MB, less than 20.47% of Python3 online submissions for Kth Largest Element in a Stream.
"""
class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.nums = sorted(nums, key=lambda x: -x)[:k]
        if len(self.nums) < k:
            self.nums.extend([None] * (k - len(self.nums)))

    def add(self, val: int) -> int:
        if self.nums[-1] is None or self.nums[-1] < val:
            if self.nums[-1] is None:
                self.nums[-1] = val

            l = 0
            r = len(self.nums) - 1
            while l <= r:
                m = (l + r) // 2
                if val < self.nums[m]:
                    l = m + 1
                elif val == self.nums[m]:
                    l = m
                    break
                else:
                    if l == r:
                        break

                    r = m

            self.nums[l:] = [val] + self.nums[l:-1]

        return self.nums[-1]


"""
Runtime: 3860 ms, faster than 5.01% of Python3 online submissions for Kth Largest Element in a Stream.
Memory Usage: 18.5 MB, less than 11.58% of Python3 online submissions for Kth Largest Element in a Stream.
"""
class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.nums = sorted(nums, key=lambda x: -x)[:k]
        if len(self.nums) < k:
            self.nums.extend([None] * (k - len(self.nums)))

    def add(self, val: int) -> int:
        if self.nums[-1] is None or self.nums[-1] < val:
            self.nums[-1] = val
            self.nums.sort(key=lambda x: -x)

        return self.nums[-1]


"""
Runtime: 92 ms, faster than 92.83% of Python3 online submissions for Kth Largest Element in a Stream.
Memory Usage: 18.5 MB, less than 20.47% of Python3 online submissions for Kth Largest Element in a Stream.
https://leetcode.com/problems/kth-largest-element-in-a-stream/discuss/148866/Python-simple-heapq-solution-beats-100
"""
class KthLargest:
    def __init__(self, k, nums):
        self.pool = nums
        self.k = k
        heapq.heapify(self.pool)
        while len(self.pool) > k:
            heapq.heappop(self.pool)

    def add(self, val):
        if len(self.pool) < self.k:
            heapq.heappush(self.pool, val)
        elif val > self.pool[0]:
            heapq.heapreplace(self.pool, val)
        return self.pool[0]

