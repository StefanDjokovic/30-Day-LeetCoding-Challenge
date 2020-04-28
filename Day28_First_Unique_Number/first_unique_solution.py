# A non-efficient solution but it was able to pass the time limits constraints


class FirstUnique:

    def __init__(self, nums: List[int]):
        self.store = {}
        self.queue = []
        for i in nums:
            if i not in self.store:
                self.store[i] = 1
                self.queue.append(i)
            else:
                if self.store[i] == 1:
                    self.queue.remove(i)
                self.store[i] = self.store[i] + 1

    def showFirstUnique(self) -> int:
        if len(self.queue) > 0:
            return self.queue[0]
        else:
            return -1

    def add(self, value: int) -> None:
        if value not in self.store:
            self.store[value] = 1
            self.queue.append(value)
        else:
            if self.store[value] == 1:
                self.queue.remove(value)
            self.store[value] = self.store[value] + 1

# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)