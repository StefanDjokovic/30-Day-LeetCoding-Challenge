# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, x: int, y: int) -> int:
#    def dimensions(self) -> list[]:


# Interactive problem, used a binary search
def get_mid(l, h):
    return (l + h) // 2

def get_options(mid, available, binaryMatrix):
    opt = []
    for r in available:
        if binaryMatrix.get(r, mid) == 1:
            opt.append(r)
    return opt

class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        q = BinaryMatrix.dimensions(binaryMatrix)
        N = int(q[0])
        M = int(q[1])
        l = 0
        h = M - 1
        available = [i for i in range(N)]
        change = 0
        while l <= h:
            mid = get_mid(l, h)
            check_options = get_options(mid, available, binaryMatrix)
            if len(check_options) == 0:
                l = mid + 1
            else:
                available = check_options
                h = mid - 1
                change += 1
        if change == 0 or len(available) == 0:
            return -1
        else:
            return l