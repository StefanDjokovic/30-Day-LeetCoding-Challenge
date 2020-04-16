# The code is kinda ugly, but this was a fun way to solve this. There are many interesting edge cases that
#   were all solved by running the same thing in reverse


class Solution:
    def checkValidString(self, s: str) -> bool:
        ast = 0
        ast_only_left = 0
        left = 0
        right = 0

        for char in s:
            if char == '*':
                ast += 1
            if char == '(':
                left += 1
            if char == ')':
                right += 1
                if right > left:
                    if ast_only_left > 0:
                        ast_only_left -= 1
                        left += 1
                    elif ast > 0:
                        ast -= 1
                        left += 1
                    else:
                        return False
            if right == left:
                ast_only_left += ast
                ast = 0

        if left - right > ast:
            return False

        ast = 0
        ast_only_left = 0
        left = 0
        right = 0

        for char in reversed(s):
            if char == '*':
                ast += 1
            if char == '(':
                left += 1
                if left > right:
                    if ast_only_left > 0:
                        ast_only_left -= 1
                        right += 1
                    elif ast > 0:
                        ast -= 1
                        right += 1
                    else:
                        return False
            if char == ')':
                right += 1

            if right == left:
                ast_only_left += ast
                ast = 0

        if right - left > ast:
            return False

        return True
