# Dict implementation, will do the in-place implementation later

class SolutionWithDicts:
    def singleNumber(self, nums: List[int]) -> int:
        dict = {};
        
        for val in nums:
            if (val in dict):
                del dict[val]
            else:
                dict[val] = 1
  
        for key in dict:
            return key
