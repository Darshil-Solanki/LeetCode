class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        cnt = Counter(text)
        max_p = min(cnt["l"], cnt["o"])//2
        return min(max_p, cnt["a"], cnt["b"], cnt["n"])
