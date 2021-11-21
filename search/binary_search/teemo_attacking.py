# 495 https://leetcode.com/problems/teemo-attacking/

class Solution(object):
    """
    Time Limit Exceeded
    """
    def findPoisonedDuration(self, timeSeries, duration):
        return len(set(t + d for t in timeSeries for d in range(duration)))

    """
    Runtime: 2536 ms, faster than 5.31% of Python online submissions for Teemo Attacking.
    Memory Usage: 278.7 MB, less than 10.18% of Python online submissions for Teemo Attacking.
    
    Unsorted
    """
    def findPoisonedDuration(self, timeSeries, duration):
        p_set = set()
        for x in timeSeries:
            left = x
            right = x + duration - 1
            l_in = left in p_set
            r_in = right in p_set
            if l_in and r_in:
                continue

            if l_in != r_in:
                while left <= right:
                    mid = (left + right) // 2
                    if mid in p_set:
                        if l_in:
                            if mid + 1 not in p_set:
                                mid += 1
                                break
                            left = mid + 1
                        else:
                            if mid - 1 not in p_set:
                                mid -= 1
                                break
                            right = mid - 1
                    else:
                        if l_in:
                            if mid - 1 in p_set:
                                break
                            else:
                                right = mid - 1
                        else:
                            if mid + 1 in p_set:
                                break
                            else:
                                left = mid + 1

                if l_in:
                    left = mid
                    right = x + duration - 1
                else:
                    left = x
                    right = mid

            for p in range(left, right + 1):
                p_set.add(p)

        return len(p_set)

    """
    Runtime: 212 ms, faster than 81.86% of Python online submissions for Teemo Attacking.
    Memory Usage: 14.7 MB, less than 84.07% of Python online submissions for Teemo Attacking.
    """
    def findPoisonedDuration(self, timeSeries, duration):
        ans = duration * len(timeSeries)
        for i in range(1, len(timeSeries)):
            ans -= max(0, timeSeries[i - 1] + duration - timeSeries[i])

        return ans
