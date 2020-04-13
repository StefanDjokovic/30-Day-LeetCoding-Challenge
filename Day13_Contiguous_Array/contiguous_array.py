# Linear solution with dicts


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:

        n_difference = 0

        appeared = {}
        max_dist = 0
        appeared[0] = 0

        for index, i in enumerate(nums):
            if i == 0:
                n_difference += -1
            else:
                n_difference += 1
            if n_difference in appeared:
                if index + 1 - appeared[n_difference] > max_dist:
                    max_dist = index + 1 - appeared[n_difference]
            else:
                appeared[n_difference] = index + 1

        return max_dist
