class Solution:
    def decimalRepresentation(self, n: int) -> List[int]:
        ans = []
        i = 0
        while n>0:
            temp = (n%10)*(10**i)
            if temp:
                ans.append(temp)
            n//=10
            i += 1
        return ans[::-1]
