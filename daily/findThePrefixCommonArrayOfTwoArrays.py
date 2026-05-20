class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        ans = []
        tot = 0
        seen = set()
        for a, b in zip(A, B):
            if a in seen:
                tot += 1
            else:
                seen.add(a)
            if b in seen:
                tot += 1
            else:
                seen.add(b)
            ans.append(tot)
        return ans
        
        # ans = []
        # common = 0
        # cnt_a, cnt_b = Counter(), Counter()
        # for a, b in zip(A, B):
        #     if a==b:
        #         common += 1
        #         ans.append(common)
        #         continue
        #     cnt_a[a] += 1
        #     cnt_b[b] += 1
        #     temp = list(cnt_a.items())
        #     for a, c in temp:
        #         if a in cnt_b:
        #             mn_c = min(c, cnt_b[a])
        #             common += mn_c
        #             cnt_a[a] -= mn_c
        #             cnt_b[a] -= mn_c
        #             if cnt_a[a] == 0:
        #                 del cnt_a[a]
        #             if cnt_b[a] == 0:
        #                 del cnt_b[a]
        #     ans.append(common)
        # return ans
            
