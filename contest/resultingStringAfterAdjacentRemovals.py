class Solution:
    def resultingString(self, s: str) -> str:
        stack = []
        for c in s:
            if stack and ((ord(c) - ord(stack[-1])) % 26 in (1, 25)):
                stack.pop()
            else:
                stack.append(c)

        return "".join(stack)
        
        # contest code TLE 904/919
        # ans = list(s)
        # n = len(s)
        # heap = []
        
        # for i in range(n-1):
        #     diff = abs(ord(s[i])-ord(s[i+1]))
        #     if  diff == 1:
        #         heappush(heap, (i, i+1))
        #     elif diff == 25:
        #         heappush(heap, (i, i+1))

        # while heap:
        #     a_idx, b_idx = heappop(heap)
        #     if ans[a_idx] and ans[b_idx]:
        #         ans[a_idx] = ans[b_idx] = ""
        #         if a_idx>0 and b_idx<n-1:
        #             while a_idx>0 and not ans[a_idx]:
        #                 a_idx -= 1
        #             while b_idx<n-1 and not ans[b_idx]:
        #                 b_idx += 1
        #             a,b = ans[a_idx], ans[b_idx]
        #             if a and b and (abs(ord(a)-ord(b))==1 or abs(ord(a)-ord(b))==25):
        #                 heappush(heap, (a_idx, b_idx))

        # return "".join(ans)
