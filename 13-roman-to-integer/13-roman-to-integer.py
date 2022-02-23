class Solution:
    def romanToInt(self, s: str) -> int:
        lookup = {
            'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000
        }
        result = 0
        for i in range(len(s)-1):
            if lookup[s[i+1]]>lookup[s[i]]:
                result -= lookup[s[i]]
            else:
                result += lookup[s[i]]
        
        return result+lookup[s[-1]]