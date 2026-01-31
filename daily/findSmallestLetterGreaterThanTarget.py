class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        ans = "{"
        for ch in letters:
            if ch>target:
                ans = min(ans, ch)

        if ans == '{': return letters[0]
        return ans
