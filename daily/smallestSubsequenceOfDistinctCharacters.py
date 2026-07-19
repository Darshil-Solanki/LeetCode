class Solution:
    def smallestSubsequence(self, s: str) -> str:
        remaining_cnt = Counter(s)
        seen = [0] * 26

        stack = []

        for ch in s:
            idx = ord(ch) - ord("a")
            if not seen[idx]:
                while stack and stack[-1] > ch:
                    if remaining_cnt[stack[-1]] > 0:
                        top_idx = ord(stack[-1]) - ord("a")
                        seen[top_idx] = 0
                        stack.pop()
                    else:
                        break
                seen[idx] = 1
                stack.append(ch)
            remaining_cnt[ch] -= 1
        
        return "".join(stack)
