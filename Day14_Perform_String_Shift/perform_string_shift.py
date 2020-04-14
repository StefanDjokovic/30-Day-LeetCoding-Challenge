# Solution with slicing


class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        for move in shift:
            amount = move[1] % len(s)
            if move[0] == 0:  # left shift
                s = s[amount:] + s[:amount]
            elif move[0] == 1:  # right shift
                s = s[-amount:] + s[:-amount]

        return s
