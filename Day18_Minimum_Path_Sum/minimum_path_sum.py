# There is also an in-place solution, but this was the fastest to code


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        values = []
        for l in grid:
            temp = []
            for i in range(len(l)):
                temp.append([-1, -1])
            values.append(temp)

        def search(x, y):
            p = -1
            q = -1
            if x < len(grid) - 1:
                if values[x + 1][y][0] == -1:
                    values[x + 1][y][0] = search(x + 1, y)
                p = values[x + 1][y][0]

            if y < len(grid[x]) - 1:
                if values[x][y + 1][1] == -1:
                    values[x][y + 1][1] = search(x, y + 1)
                q = values[x][y + 1][1]

            if p == -1 and q == -1:
                return grid[x][y]
            elif q == -1:
                return grid[x][y] + p
            elif p == -1:
                return grid[x][y] + q
            else:
                return grid[x][y] + min(p, q)

        return search(0, 0)