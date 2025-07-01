class Solution:
    def possibleStringCount(self, word: str) -> int:
        ans = 0
        prev = word[0]
        cnt = 1
        
        for c in word[1:]:
            if c == prev:
                cnt+=1
            else:
                ans += cnt-1
                prev=c
                cnt=1
        
        ans += cnt-1
        return 1+ans
    
        # from editorial
        # ans = 1

        # for i in range(1, len(word)):
        #     if word[i-1] == word[i]:
        #         ans += 1
        
        # return ans
