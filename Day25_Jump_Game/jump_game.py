# Easy linear approach


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        reached = 0
        for index, i in enumerate(nums):
            if reached < index:
                return False
            if index + i > reached:
                reached = index + i

        return True