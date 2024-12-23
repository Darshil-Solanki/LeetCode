class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        left, ans, temp = 0, 0, 0
        vowel = "aeiou"
        for right, c in enumerate(s):
            if c in vowel:
                temp+=1
            if right-left+1>k:
                if s[left] in vowel:
                    temp-=1
                left+=1
            ans = max(ans, temp)
        return ans

        # faster solution
        # vowels = "aeiou"
        # v = 0
        # for char in s[:k]:
        #     if char in vowels:
        #         v += 1
        
        # max_v = v
        # for i in range(len(s)-k):
        #     if s[i] in vowels:
        #         v -= 1
        #     if s[i+k] in vowels:
        #         v += 1
        #     if v > max_v:
        #         max_v = v
        # return max_v
