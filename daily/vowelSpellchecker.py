class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        ans = [""]*len(queries)
        word_hash_set =  Counter(wordlist)
        case_insensitive_hash_set = {}
        vowel_mask_hash_set = {}

        def vowel_mask(word):
            return "".join('*' if c in 'AEIOU' else c for c in word)

        for w in wordlist:
            W = w.upper()
            case_insensitive_hash_set.setdefault(W, w)
            vowel_mask_hash_set.setdefault(vowel_mask(W), w)
            
        for i, q in enumerate(queries):
            if q in word_hash_set:
                ans[i] = q
                continue
            Q = q.upper()
            if Q in case_insensitive_hash_set:
                ans[i] = case_insensitive_hash_set[Q]
                continue
            
            mask = vowel_mask(Q)
            if mask in vowel_mask_hash_set:
                ans[i] = vowel_mask_hash_set[mask]
            
        return ans
            
