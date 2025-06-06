class Solution:
    def robotWithString(self, s: str) -> str:
        cnt = Counter(s)
        stack = []
        result = []
        min_char = "a"
        
        for c in s:
            stack.append(c)
            cnt[c] -= 1
            while min_char != 'z' and cnt[min_char] == 0:
                min_char = chr(ord(min_char)+1)
            while stack and stack[-1] <= min_char:
                result.append(stack.pop())
        
        return "".join(result)
