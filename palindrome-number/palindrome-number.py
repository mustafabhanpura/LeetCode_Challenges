class Solution:
    def isPalindrome(self, x: int) -> bool:
        digits = str(x)
        i = 0
        j = len(digits)-1
        flag = 'True'
        while flag == 'True' and i<=j:
            if digits[i] == digits[j]:
                i+=1
                j = j-1
            else:
                flag = 'False'
        if flag =='True':
            return True
        else:
            return False