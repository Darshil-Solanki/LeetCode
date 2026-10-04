class Solution:
    def minRotations(self, n: int, s: str) -> int:
        prefix_ans = [0]
        suffix_ans = [0]
        
        pointer = int(s[-1])
        for c in s[::-1]:
            digit = int(c)
            if pointer == digit:
                suffix_ans.append(suffix_ans[-1])
                continue
            temp = 0
            if pointer < digit:
                temp = min(digit-pointer, pointer+10-digit)
            else:
                temp = min(pointer-digit, 10-pointer+digit)
            suffix_ans.append(suffix_ans[-1]+temp)
            pointer = digit

        suffix_ans.reverse()

        pointer = 0
        ans = float("inf")
        last_point = int(s[-1])
        def cost_to_last(digit):
            if digit == last_point:
                return 0
            if last_point < digit:
                return min(digit-last_point, last_point+10-digit)
            return min(last_point-digit, 10-last_point+digit)
            
        for i, c in enumerate(s):
            digit = int(c)
            if pointer == digit:
                prefix_ans.append(prefix_ans[-1])
                ans = min(ans, prefix_ans[-1]+suffix_ans[i+1]+cost_to_last(digit))
                continue
            temp = 0
            if pointer < digit:
                temp = min(digit-pointer, pointer+10-digit)
            else:
                temp = min(pointer-digit, 10-pointer+digit)
            prefix_ans.append(prefix_ans[-1]+temp)
            ans = min(ans, prefix_ans[-1]+suffix_ans[i+1]+cost_to_last(digit))
            pointer = digit

        ans = min(ans, prefix_ans[-1], suffix_ans[0]+cost_to_last(0))
        
        return ans 
