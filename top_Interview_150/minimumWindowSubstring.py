class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or len(t)>len(s): return ""
        currCounter = Counter()
        left, charCounter = 0, Counter(t)
        have , need = 0, len(charCounter)
        res, resLen = (-1,-1), float('inf')
        for right in range(len(s)):
            c=s[right]
            currCounter[c]+=1
            if c in charCounter and currCounter[c]==charCounter[c]:
                have+=1
            while have==need:
                if right-left+1<resLen:
                    resLen=right-left+1
                    res=(left, right)
                currCounter[s[left]]-=1
                if s[left] in charCounter and currCounter[s[left]]<charCounter[s[left]]:
                    have-=1
                left+=1
        l, r = res
        return s[l:r+1] if resLen<float('inf') else ""
