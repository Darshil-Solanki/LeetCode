class Solution:
    def maxFreqSum(self, s: str) -> int:
        c = Counter(s)
        vowel_count = consonant_count = 0
        
        for vowel in "aeiou":
            vowel_count = max(c[vowel], vowel_count)
        for consonant in "bcdfghjklmnpqrstvwxyz":
            consonant_count = max(c[consonant], consonant_count)

        return vowel_count + consonant_count
            
