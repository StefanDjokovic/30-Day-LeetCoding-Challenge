class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        tot = 0
        vals = {}
        for index, i in enumerate(nums):
            nums[index] = tot
            tot += i
            if tot not in vals:
                vals[tot] = [index]
            else:
                vals[tot] = vals[tot] + [index]
        nums.append(tot)

        count = 0
        for index, i in enumerate(nums):
            if (k + i) in vals:
                for comb in vals[k + i]:
                    print(comb)
                    if comb >= index:
                        count += 1

        return count
