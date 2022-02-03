class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 1 or len(s)==0:
            return False
        stack = []
        lookup = {
            ')':'(',
            '}':'{',
            ']':'['     
        }
        for bracket in s:
            if bracket in ('(','{','['):
                stack.append(bracket)
            elif bracket in lookup.keys() and len(stack)==0:
                return False
            else:
                if lookup[bracket] == stack[-1]:
                    stack.pop()
                else:
                    return False
        if len(stack) == 0:
            return True
        else:
            return False
                