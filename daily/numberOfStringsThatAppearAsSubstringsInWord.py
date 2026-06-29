class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        n = len(word)

        def check(pattern):
            m = len(pattern)
            pi = [0]*m
            j = 0
            
            for i in range(1, m):
                while j and pattern[i]!=pattern[j]:
                    j = pi[j-1]
                if pattern[i]==pattern[j]:
                    j += 1
                pi[i] = j
            
            j = 0
            for i in range(n):
                while j and word[i] != pattern[j]:
                    j = pi[j-1]
                if word[i] == pattern[j]:
                    j += 1
                if j == m:
                    return True
            
            return False

        return sum(check(p) for p in patterns)
        # below method is still faster for runtime because of smaller length of word and patterns and patterns[i]
        # return sum(p in word for p in patterns)
