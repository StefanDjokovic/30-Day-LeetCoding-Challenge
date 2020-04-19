# The obvious O(n) solution, it can be done in O(logn) with binary search and checking the "ordered" array, pretty neat


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        for index, i in enumerate(nums):
            if i == target:
                return index
        return -1