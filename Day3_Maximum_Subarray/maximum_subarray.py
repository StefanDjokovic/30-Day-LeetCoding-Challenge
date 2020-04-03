# time: O(N), space: O(1), with a dynamic programming approach, pretty fun!


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        maxVal = nums[0]
        for index in range(1, len(nums)):
            val = nums[index]
            sumVal = val + nums[index - 1]
            if sumVal > val:
                nums[index] = sumVal

            if nums[index] > maxVal:
                maxVal = nums[index]

        return maxVal
