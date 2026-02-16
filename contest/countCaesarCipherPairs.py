class Solution:
    def countPairs(self, words: List[str]) -> int:
        n, m = len(words), len(words[0])
        word_mask_count = defaultdict(int)

        ans = 0
        for i, word in enumerate(words):
            curr_mask = tuple((26-(ord(c)-97)%26)%26 for c in word)
            for t in range(26):
                new_mask = tuple((mask+t)%26 for mask in curr_mask)
                if new_mask in word_mask_count:
                    ans += word_mask_count[new_mask]
                    
            word_mask_count[curr_mask] += 1

        return ans
