class Solution:
    def countBits(self, n: int) -> List[int]:
        
        ret = []
        for i in range(n+1):
            ret.append(bin(i)[2:].count('1'))
        return ret 