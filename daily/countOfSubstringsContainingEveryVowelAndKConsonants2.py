class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        n = len(word)
        
        def is_vowel(c):
            return c in "aeiou"
        def at_least(k):
            vowel_counts = defaultdict(int)
            cons_counts = 0
            left = ans = 0
            for right in range(n):
                c = word[right]
                if is_vowel(c):
                    vowel_counts[c]+=1
                else:
                    cons_counts +=1 

                while len(vowel_counts)==5 and cons_counts>=k:
                    ans += n-right
                    if is_vowel(word[left]):
                        vowel_counts[word[left]]-=1
                        if not vowel_counts[word[left]]: del vowel_counts[word[left]]
                    else:
                        cons_counts-=1
                    left+=1

            return ans
        
        return at_least(k)-at_least(k+1)
