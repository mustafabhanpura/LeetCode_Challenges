class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        seperated_str = s.split(' ')
        valid_str = [word for word in seperated_str if word != '']
        return(len(valid_str[-1]))