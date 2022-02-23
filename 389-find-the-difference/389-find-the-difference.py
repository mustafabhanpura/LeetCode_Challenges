from collections import Counter

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s_dict = Counter(s)
        t_dict = Counter(t)
        result= []
        for char in t_dict.keys():
            if char in s_dict:
                if t_dict[char]!=s_dict[char]:
                    result.append(char)
            else:
                result.append(char)
        return ''.join(result)