class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        ans = []

        def can_edit(word, target):
            diff = 0
            for w, t in zip(word, target):
                if w!=t:
                    diff += 1
                if diff==3:
                    return False
            return diff<=2

        for word in queries:
            for d_word in dictionary:
                if can_edit(word, d_word):
                    ans.append(word)
                    break
        return ans
