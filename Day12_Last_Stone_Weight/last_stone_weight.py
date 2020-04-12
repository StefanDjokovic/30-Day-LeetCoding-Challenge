# Easy solution by taking away the two highest values and then adding the new result back

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        while len(stones) > 1:
            first = max(stones)
            stones.remove(first)
            second = max(stones)
            stones.remove(second)

            if first > second:
                stones.append(first - second)

        if len(stones) == 1:
            return stones[0]
        return 0