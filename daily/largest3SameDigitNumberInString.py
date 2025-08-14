class Solution:
    def largestGoodInteger(self, num: str) -> str:
        count = 1
        ans = -1
        prev = ""

        for n in num:
            if n==prev:
                count += 1
                if count==3:
                    ans = max(ans, int(n))
            else:
                count = 1
            prev = n
        
        return "" if ans==-1 else str(ans)*3


        # cnt = Counter(num[:3])
        # ans = int(num[0]) if len(cnt)==1 else -1
        
        # for i in range(3, len(num)):
        #     cnt[num[i]] += 1
        #     cnt[num[i-3]] -= 1
        #     if cnt[num[i-3]] == 0:
        #         del cnt[num[i-3]]
            
        #     if len(cnt)==1:
        #         ans = max(ans, int(num[i]))

        # return "" if ans==-1 else str(ans)*3
         s
