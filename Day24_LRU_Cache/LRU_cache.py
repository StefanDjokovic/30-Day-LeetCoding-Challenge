# I'm still terrible with Python data structures and I had to look into the Leetcode discussions to find
# pretty neat solution with OrderedDict!

from collections import OrderedDict


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.values = OrderedDict()

    def get(self, key: int) -> int:
        if key in self.values:
            val = self.values.pop(key)
            self.values[key] = val
            return val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if not self.values.pop(key, None) and self.capacity == len(self.values):
            self.values.popitem(last=False)
        self.values[key] = value

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)