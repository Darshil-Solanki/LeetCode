class Solution:
    def longestSubsequenceRepeatedK(self, s: str, k: int) -> str:
        cnt = Counter(s)
        candidate = []

        for c, times in cnt.items():
            if times>=k:
                candidate.append(c)
        
        candidate.sort(reverse = True)
        ans = ""  
        queue = deque(candidate)
        while queue:
            curr_chr = queue.popleft()
            if len(curr_chr)>len(ans):
                ans = curr_chr
            for ch in candidate:
                next_chr = curr_chr + ch
                it = iter(s)
                if all(c in it for c in next_chr*k):
                    queue.append(next_chr)
        
        return ans
