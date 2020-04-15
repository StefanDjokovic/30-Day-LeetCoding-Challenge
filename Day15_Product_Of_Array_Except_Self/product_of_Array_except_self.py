# O(n) solution, but not respecting the "note" (which says to not use divisions)


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product_without_zero = 1
        pos_zero = -1

        print(nums)
        for index, i in enumerate(nums):
            if i != 0:
                product_without_zero *= i
            elif pos_zero == -1:
                pos_zero = index
            else:
                pos_zero = -2

        if pos_zero == -2:
            for index in range(len(nums)):
                nums[index] = int(0)
        elif pos_zero != -1:
            for index in range(len(nums)):
                if index != pos_zero:
                    nums[index] = 0
                else:
                    nums[index] = product_without_zero
        else:
            for index, i in enumerate(nums):
                nums[index] = product_without_zero // i

        return nums
