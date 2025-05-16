class Solution:
    def getWordsInLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        
        def check_hamming_distance(word1, word2):
            if len(word1)!=len(word2):
                return False
            
            diff = 0
            for c1, c2 in zip(word1, word2):
                if c1!=c2:
                    diff  += 1
                if diff>1: return False
            
            return True
        
        n = len(groups)
        dp = [1]*n
        prev = [-1]*n
        max_index = 0

        for i in range(1, n):
            for j in range(i):
                if (check_hamming_distance(words[i], words[j]) 
                    and dp[j]+1>dp[i] 
                    and groups[i]!=groups[j]): 
                    dp[i] = dp[j]+1
                    prev[i] = j
                if dp[i]>dp[max_index]:
                    max_index = i
            
        ans = []
        while max_index >= 0:
            ans.append(words[max_index])
            max_index = prev[max_index]
        
        ans.reverse()
        return ans
