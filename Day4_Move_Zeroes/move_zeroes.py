# Lists in Python are so much fun

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nPushed = 0
        if len(nums) == 1:
            return
        for i in range(len(nums)):
            while len(nums) > i and nums[i] == 0:
                nPushed += 1
                del nums[i]
        for i in range(nPushed):
            nums.append(0)