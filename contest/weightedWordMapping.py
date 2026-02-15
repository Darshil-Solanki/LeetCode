class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        ans = []
        for word in words:
            weight = 0
            for c in word:
                weight += weights[ord(c)-97]
            ans.append(chr(122-(weight%26)))
        return "".join(ans)
