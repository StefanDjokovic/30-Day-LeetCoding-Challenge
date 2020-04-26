# Solved with the Smith-Waterman algorithm


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        mat = []
        for i in range(len(text2) + 1):
            mat.append([0 for i in range(len(text1) + 1)])
        text1 = "$" + text1
        text2 = "$" + text2

        curr_max = 0
        for index_i, i in enumerate(text2):
            for index_j, j in enumerate(text1):
                if j != '$' and i != '$':
                    if text2[index_i] == text1[index_j]:
                        mat[index_i][index_j] = mat[index_i - 1][index_j - 1] + 1
                    else:
                        mat[index_i][index_j] = mat[index_i - 1][index_j - 1]
                    mat[index_i][index_j] = max(mat[index_i][index_j], mat[index_i - 1][index_j],
                                                mat[index_i][index_j - 1])

                if mat[index_i][index_j] > curr_max:
                    curr_max = mat[index_i][index_j]

        return curr_max