







# O(n+m) space and time solution

class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        actual_s = []
        for char in S:
            if char != '#':
                actual_s.append(char)
            elif len(actual_s) > 0:
                del actual_s[-1]

        actual_s = "".join(actual_s)
        # print(actual_s)

        actual_t = []
        for char in T:
            if char != '#':
                actual_t.append(char)
            elif len(actual_t) > 0:
                del actual_t[-1]

        actual_t = "".join(actual_t)
        # print(actual_t)

        if actual_s == actual_t:
            return True
        return False

