class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        ans = s.count("1")
        new_transformed = [s[0]]
        count = [1]
        i = 1
        prev = s[0]
        while i<len(s):
            curr = s[i]
            if curr==prev:
                count[-1]+=1
            else:
                new_transformed.append(curr)
                count.append(1)
            prev = curr
            i+=1

        tot_active = ans 
        for i, c in enumerate(new_transformed):
            if c=="1":
                if i>0 and new_transformed[i-1]=="0" and i+1<len(new_transformed) and new_transformed[i+1]=="0":
                    ans = max(ans, count[i-1]+count[i+1]+tot_active)

        return ans
