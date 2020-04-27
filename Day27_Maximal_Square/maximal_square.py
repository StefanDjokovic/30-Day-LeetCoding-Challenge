# I used the typical dynamic approach to get the total sum of the values in the rectangle from the origin to the
# corresponding element in the matrix. Then checked for each cell going to the diagonal if the value in the next
# position is == size * size, which would mean that all the 1s are filled.


def sum_square(matrix, r_max, c_max, r_min, c_min):
    if r_min > 0:
        upper_row = matrix[r_min - 1][c_max]
    else:
        upper_row = 0

    if c_min > 0:
        left_col = matrix[r_max][c_min - 1]
    else:
        left_col = 0

    if r_min > 0 and c_min > 0:
        intersection = matrix[r_min - 1][c_min - 1]
    else:
        intersection = 0
    return matrix[r_max][c_max] - (upper_row + left_col - intersection)


def search_max_square(matrix, r, c, size):
    if sum_square(matrix, r + size - 1, c + size - 1, r, c) == size * size:
        if r + size < len(matrix) and c + size < len(matrix[r]):
            return search_max_square(matrix, r, c, size + 1)
        else:
            return size * size
    else:
        return (size - 1) * (size - 1)


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                matrix[i][j] = int(matrix[i][j])
                # if i > 0:
                #     matrix[i][j] += int(matrix[i-1][j])
                if j > 0:
                    matrix[i][j] += int(matrix[i][j - 1])
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                matrix[i][j] = int(matrix[i][j])
                if i > 0:
                    matrix[i][j] += int(matrix[i - 1][j])

        max_found = 0

        for r in range(len(matrix)):
            for c in range(len(matrix[r])):
                max_found = max(max_found, search_max_square(matrix, r, c, 1))

        return max_found