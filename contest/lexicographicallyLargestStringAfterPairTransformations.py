class Solution:
    def largestString(self, nums: list[int]) -> list[str]:
        ans = []

        @cache
        def get_result(num):
            stack = [(num, "a")]
            while stack[-1][0]>1:
                times, ch = stack.pop()
                if ord(ch)==122:
                    stack.append((times, ch))
                    break
                if times%2:
                    stack.append((1, ch))
                    times -= 1
                stack.append((times//2, chr(ord(ch)+1)))

            return "".join((c*_ if c=="z" else c) for _, c in stack[::-1])
            
        for num in nums:
            ans.append(get_result(num))

        return ans
