class Solution:
    def findMismatchedSegments(self, s1: str, s2: str) -> list[list[str]]:
        n = len(s1)
        i = 0
        ans = []

        while i<n:
            st = i
            while i<n and s1[i] != s2[i]:
                i += 1

            if st!=i:
                ans.append([s1[st:i], s2[st:i]])
                continue
            i += 1
            
        return ans
