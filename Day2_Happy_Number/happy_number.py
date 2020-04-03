# First solution, converting the number to a string and iterating through it (slow)


class Solution:
    def isHappy(self, n: int) -> bool:
        
        steps = set()
        steps.add(n)
        
        while n != 1:
            val = 0
            for d in str(n):
                val = val + int(d)*int(d)
            n = val
            ptLen = len(steps)
            steps.add(n)
            if ptLen == len(steps):
                return False
        return True
        
        
# Second solution: typical module + divide operations to get the single digits (faster than 88.07%)

class Solution2:
    def isHappy(self, n: int) -> bool:
        
        steps = set()
        steps.add(n)
        
        while n != 1:
            val = 0
            while n != 0:
                val += (n % 10)**2
                n = n // 10
            n = val
            ptLen = len(steps)
            steps.add(n)
            if ptLen == len(steps):
                return False
        return True
        
        
# Instead of checking the difference between the length of the new and old sets, 
# checked if the new n is in the set (speed same as above, 88.07%)

class Solution3:
    def isHappy(self, n: int) -> bool:
        
        steps = set()
        steps.add(n)
        
        while n != 1:
            val = 0
            while n != 0:
                val += (n % 10)**2
                n = n // 10
            n = val
            if n in steps:
                return False
            else:
                steps.add(n)
        return True
