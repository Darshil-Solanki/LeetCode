class Solution:
    def possibleStringCount(self, word: str) -> int:
        # Copied from contest result
        runs = []
        prev = word[0]
        cnt = 1
        for c in word[1:]:
            if c == prev:
                cnt+=1
            else:
                runs.append(cnt)
                prev=c
                cnt=1
        runs.append(cnt)
        return 1 + sum(r-1 for r in runs)
