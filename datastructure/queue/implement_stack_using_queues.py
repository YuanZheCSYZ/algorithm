# 225 https://leetcode.com/problems/implement-stack-using-queues/submissions/

"""
Runtime: 28 ms, faster than 81.64% of Python3 online submissions for Implement Stack using Queues.
Memory Usage: 14.3 MB, less than 44.98% of Python3 online submissions for Implement Stack using Queues.
"""
class MyStack:
    def __init__(self):
        self.q1 = []
        self.reveresed = False

    def push(self, x: int) -> None:
        if self.reveresed:
            self.q1.append(self.q1.pop(0))
            self.reveresed = False

        self.q1.append(x)
        return None

    def pop(self) -> int:
        if self.reveresed:
            self.reveresed = False
            return self.q1.pop(0)

        if self.q1:
            for x in range(len(self.q1) - 1):
                self.q1.append(self.q1.pop(0))

            return self.q1.pop(0)
        else:
            return None

    def top(self) -> int:
        if self.reveresed:
            return self.q1[0]

        if self.q1:
            self.reveresed = True
            for x in range(len(self.q1) - 1):
                self.q1.append(self.q1.pop(0))

            return self.q1[0]

    def empty(self) -> bool:
        return not self.q1
