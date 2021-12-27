class Solution:
    def findComplement(self, num: int) -> int:
        a = bin(num).replace("0b", "")
        output = []
        for A in a:
            if A == '0':
                output.append('1')
            else:
                output.append('0')
        binary = ''.join(output)
        return (int(binary,2))