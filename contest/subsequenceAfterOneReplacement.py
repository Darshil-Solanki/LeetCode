class Solution:
    def canMakeSubsequence(self, s: str, t: str) -> bool:
        len_s, len_t = len(s), len(t)
        
        left_match = [len_t]*len_s
        j = 0
        for i in range(len_s):
            while j<len_t and t[j]!=s[i]:
                j += 1
            
            if j < len_t:
                left_match[i] = j
                j += 1
        
        if left_match[-1]!=len_t:
            return True
        
        right_match = [-1]*len_s
        j = len_t-1
        for i in range(len_s-1, -1, -1):
            while j>-1 and t[j]!=s[i]:
                j -= 1
            if j>-1:
                right_match[i] = j
                j -= 1
        
        for skip_idx in range(len_s):
            low_bound = left_match[skip_idx - 1]
            if skip_idx == 0:
                low_bound = -1
            
            if skip_idx == len_s-1:
                high_bound = len_t
            else:
                high_bound = right_match[skip_idx+1]
            
            if low_bound<len_t and high_bound>-1 and high_bound-low_bound>1:
                return True
        
        return False
