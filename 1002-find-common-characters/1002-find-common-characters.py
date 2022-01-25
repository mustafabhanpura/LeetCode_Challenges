class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        intial = collections.Counter(words[0])
        
        for word in words:
            intial &= collections.Counter(word)
        
        return (list(intial.elements()))