class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort(reverse=True)
        return sum(h-i for i, h in enumerate(happiness[:k]) if h-i>0)
