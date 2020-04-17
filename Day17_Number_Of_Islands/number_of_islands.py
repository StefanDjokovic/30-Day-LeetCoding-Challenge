# Simple DFS search


def has_land_connection(posX, posY, grid, visited):
    visited[posX][posY] = 1
    if posX > 0:
        if visited[posX - 1][posY] == 0 and grid[posX - 1][posY] == "1":
            has_land_connection(posX - 1, posY, grid, visited)
    if posY > 0:
        if visited[posX][posY - 1] == 0 and grid[posX][posY - 1] == "1":
            has_land_connection(posX, posY - 1, grid, visited)
    if posX < len(grid) - 1:
        if visited[posX + 1][posY] == 0 and grid[posX + 1][posY] == "1":
            has_land_connection(posX + 1, posY, grid, visited)
    if posY < len(grid[posX]) - 1:
        if visited[posX][posY + 1] == 0 and grid[posX][posY + 1] == "1":
            has_land_connection(posX, posY + 1, grid, visited)


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = []
        for l in range(len(grid)):
            section = []
            for i in range(len(grid[l])):
                section.append(0)
            visited.append(section)

        count = 0
        for x in range(len(grid)):
            for y in range(len(grid[x])):
                if visited[x][y] == 0 and grid[x][y] == "1":
                    has_land_connection(x, y, grid, visited)
                    count += 1
                visited[x][y] = 1

        return count
