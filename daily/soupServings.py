class Solution:
    @cache
    def dp(self, a, b):
        if a <= 0 and b <= 0:
            return 0.5  # Both empty
        if a <= 0:
            return 1.0  # A is empty first
        if b <= 0:
            return 0.0  # B is empty first

        # Probability is average of 4 choices
        return 0.25 * (
            self.dp(a - 4, b) +
            self.dp(a - 3, b - 1) +
            self.dp(a - 2, b - 2) +
            self.dp(a - 1, b - 3)
        )

    def soupServings(self, n: int) -> float:
        # code from editorial
        if n>4300: return 1

        # Convert to units of 25 ml
        m = (n + 24) // 25
        return self.dp(m, m)
