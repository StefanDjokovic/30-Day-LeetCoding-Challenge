class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        if m == n:
            return m

        if m.bit_length() < n.bit_length():
            return 0

        ender = 2147483647

        curr_pow = 1
        if m + curr_pow <= n:
            ender = ender << 1
        else:
            return m & ender

        for i in range(1, 32):
            curr_pow *= 2
            if m + curr_pow <= n:
                ender = ender << 1
            else:
                return m & n & ender