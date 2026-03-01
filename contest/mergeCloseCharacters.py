class Solution:
    def mergeCharacters(self, s: str, k: int) -> str:
        window = deque([])
        ans = []
        curr_set = defaultdict(int)
        for right in range(len(s)):
            if len(window) <= k and s[right] not in curr_set:
                window.append(s[right])
                curr_set[s[right]] += 1
                ans.append(s[right])
            
            if len(window) > k:
                c = window.popleft()
                curr_set[c] -= 1
                if not curr_set[c]:
                    del curr_set[c]
                

        return "".join(ans)
