class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1)!=len(word2): return False
        c1, c2 = Counter(word1), Counter(word2)
        if sorted(c1.keys())!=sorted(c2.keys()): return False
        if sorted(c1.values())!=sorted(c2.values()): return False
        return True

        # faster version
        # unique_char = set(word1)
        # cc1, cc2 = [], []
        # for c in unique_char:
        #     cc1.append(word1.count(c))
        #     cc2.append(word2.count(c))
        # return sorted(cc1)==sorted(cc2)
