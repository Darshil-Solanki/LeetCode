class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:    
        cnt = Counter(s)
        ans = ""
        prefix_cnt = Counter()

        for i, t in enumerate(target):
            suffix_cnt = cnt - prefix_cnt
            
            for j in range(ord(t)+1, 123):
                c = chr(j)
                if suffix_cnt[c]>0:
                    suffix_cnt[c] -= 1
                    curr_prefix = target[:i]

                    curr_suffix = []
                    for ch, count in suffix_cnt.items():
                        curr_suffix.append(ch*count)
                    curr_suffix.sort()

                    candidate = "".join([curr_prefix, c]+curr_suffix)
                    if ans == "" or candidate < ans:
                        ans = candidate
                    
                    break

            prefix_cnt[t] += 1
            if prefix_cnt[t]>cnt[t]:
                break

        return ans
