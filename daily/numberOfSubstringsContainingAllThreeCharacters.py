class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        def is_all_char():
            return counts["a"] and counts["b"] and counts["c"]
        counts = defaultdict(int)
        n = len(s)

        left = ans =0
        for right in range(n):
            c = s[right]
            counts[c]+=1
            while is_all_char():
                ans += n-right
                counts[s[left]]-=1
                left+=1
        
        return ans

        # faster approach from submission
        # n = len(s)
        # arr = [-1, -1, -1]
        # cnt = 0
        # for i in range(n):
        #     ch = s[i]
        #     arr[ord(ch) - ord('a')] = i
        #     cnt += 1 + min(arr)
        # return cnt
