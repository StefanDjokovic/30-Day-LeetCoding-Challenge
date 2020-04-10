# Not really the best solution, retrieving should be done in constant time

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.struct = []

    def push(self, x: int) -> None:
        self.struct.append(x)

    def pop(self) -> None:
        if len(self.struct) > 0:
            del self.struct[-1]

    def top(self) -> int:
        if len(self.struct) > 0:
            return self.struct[-1]
        else:
            return None

    def getMin(self) -> int:
        if len(self.struct) > 0:
            return min(self.struct)
        else:
            return None

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()