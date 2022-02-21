class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        setenceAsList = sentence.split(" ")
        for i in range(len(setenceAsList)):
            for j in dictionary:
                if setenceAsList[i].startswith(j):
                    setenceAsList[i] = j
        return " ".join(setenceAsList)