# O(1) memory approach with the XOR operator

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        for val in nums[1:]:
            nums[0] ^= val

        return nums[0]


# Implementation with sets

class SolutionWithDicts:
    def singleNumber(self, nums: List[int]) -> int:
        valKeeper = set()

        for val in nums:
            if val in valKeeper:
                valKeeper.remove(val)
            else:
                valKeeper.add(val)

        return valKeeper.pop()
