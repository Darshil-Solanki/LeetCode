class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
        ans = float("inf")
        n = len(words)
        for i, word in enumerate(words):
            if word == target:
                ans = min((ans, abs(startIndex-i), n-startIndex+i, startIndex+n-i))
        return ans if ans!=float("inf") else -1
