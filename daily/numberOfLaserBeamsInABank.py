class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        prev = 0
        ans = 0
        first = m = len(bank)
        for i, b in enumerate(bank):
            if b.find("1")!=-1:
                first = i
                prev = b.count("1")
                break
        
        if first==m:
            return 0
        
        for i in range(first+1, m):
            cnt = bank[i].count("1")
            if cnt:
                ans += prev*cnt
                prev = cnt
            
        return ans
