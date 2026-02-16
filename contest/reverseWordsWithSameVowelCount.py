class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        def get_vowel_cnt(word):
            return sum(1 for c in word if c in "aeiou")

        first_vowel_cnt = get_vowel_cnt(words[0])
        for i in range(1, len(words)):
            vowel_cnt = get_vowel_cnt(words[i])
            if vowel_cnt == first_vowel_cnt:
                words[i] = words[i][::-1]

        return " ".join(words)
