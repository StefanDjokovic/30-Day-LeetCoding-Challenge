# Fun little problem


# First solution with dicts and without sorting!

class Solution:
    def countElements(self, arr: List[int]) -> int:

        possible_values = {}

        for i in arr:
            if i + 1 not in possible_values:
                possible_values[i + 1] = [1, 0]
            else:
                possible_values[i + 1] = [possible_values[i + 1][0] + 1, possible_values[i + 1][1]]

            if i not in possible_values:
                possible_values[i] = [0, 1]
            else:
                possible_values[i] = [possible_values[i][0], possible_values[i][1] + 1]

        print(possible_values)

        count_x = 0
        for val in possible_values.values():
            if val[1] > 0:
                count_x += val[0]

        return count_x

# A bit more optimized than the first solution, still sorting + dict

class Solution:
    def countElements(self, arr: List[int]) -> int:
        arr.sort(reverse=True)

        possible_values = {}

        for i in arr:
            possible_values[i] = 0

            if i + 1 in possible_values:
                possible_values[i + 1] += 1

        # print(possible_values)

        count_x = 0
        for val in possible_values.values():
            count_x += val

        return count_x



# First solution that came to my mind mind

class Solution:
    def countElements(self, arr: List[int]) -> int:
        arr.sort()

        possible_values = {}

        for i in arr:
            if i + 1 not in possible_values:
                possible_values[i + 1] = [1, 0]
            else:
                possible_values[i + 1] = [possible_values[i + 1][0] + 1, possible_values[i + 1][1]]

            if i in possible_values:
                possible_values[i] = [possible_values[i][0], possible_values[i][1] + 1]

        print(possible_values)

        count_x = 0
        for val in possible_values.values():
            if val[1] > 0:
                count_x += val[0]

        return count_x
