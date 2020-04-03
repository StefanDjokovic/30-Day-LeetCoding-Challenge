# O(1) memory approach with the XOR operator

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        for val in nums[1:]:
            nums[0] ^= val

        return nums[0]


# first implementation with dicts (Sets would have been better)

class SolutionWithDicts:
    def singleNumber(self, nums: List[int]) -> int:
        valKeeper = {};

        for val in nums:
            if val in valKeeper:
                del valKeeper[val]
            else:
                valKeeper[val] = 1

        for key in valKeeper:
            return key