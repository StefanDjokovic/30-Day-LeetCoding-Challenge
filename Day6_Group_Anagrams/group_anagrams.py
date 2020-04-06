class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        word_dict = {}

        for s in strs:
            o = ''.join(sorted(s))
            if o in word_dict:
                word_dict[o].append(s)

            else:
                word_dict[o] = [s]

        return [value for value in word_dict.values()]
