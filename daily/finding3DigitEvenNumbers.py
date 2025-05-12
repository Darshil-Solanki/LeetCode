class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        cnt = Counter(digits)
        res = []

        for a in range(1, 10):
            if not cnt[a]: continue # digit is not in digits
            cnt[a] -= 1
            for b in range(10):
                if not cnt[b]: continue
                cnt[b] -= 1
                for c in (0, 2, 4, 6, 8):
                    if cnt[c]:
                        res.append(a*100 + b*10 + c)
                cnt[b] += 1
            cnt[a] += 1
        
        return res

        # digits.sort()
        # n = len(digits)
        # res = set()
        # for i, first in enumerate(digits):
        #     if first:
        #         for j, second in enumerate(digits):
        #             if j!=i:
        #                 for k, third in enumerate(digits):
        #                     if k!=j and k!=i and third%2 == 0:
        #                         res.add(first*100 + second*10 +third)
        
        # return list(sorted(res))
