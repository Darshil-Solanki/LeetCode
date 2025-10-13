class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        # return [next(g) for _, g in groupby(words, sorted)]

        i = 0
        ans = []
        
        while i<len(words):
            j = i+1
            a = sorted(words[i])
            while j<len(words) and a == sorted(words[j]):
                j += 1
            ans.append(words[i])
            i = j
        
        return ans
