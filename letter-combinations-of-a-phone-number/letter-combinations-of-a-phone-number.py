import itertools
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        library = {
            "1":"",
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz"
        }
        result = [""]
        if len(digits) == 0:
            return []
        for digit in digits:
            chars = library[digit]
            new_result = []
            for char in chars:
                for string in result:
                    new_result.append(string+char)
            result = new_result
        
        return result