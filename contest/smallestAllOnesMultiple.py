class Solution:
    def minAllOneMultiple(self, k: int) -> int:
        if k%2==0: return -1
        if k%5==0: return -1
        str_k = str(k)
        if str_k.count("1") == len(str_k): return len(str_k)
        ans = len(str_k)
        num = int("1"*len(str_k))
        
        while num%k!=0:
            num = ((num%k)*10)+1
            ans += 1
            
        return ans
