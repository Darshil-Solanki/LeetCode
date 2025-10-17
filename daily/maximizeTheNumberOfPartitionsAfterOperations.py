class Solution:
    def maxPartitionsAfterOperations(self, s: str, k: int) -> int:
        n = len(s)
        left_partition = [(0, 0, 0) for _ in range(n)]
        right_partition = [(0, 0, 0) for _ in range(n)]

        num = mask = count = 0
        for i in range(n-1):
            binary = 1 << (ord(s[i]) - 97)
            if not (mask & binary):
                count += 1
                if count<=k:
                    mask |= binary
                else:
                    num += 1
                    mask = binary
                    count = 1
            left_partition[i+1] = (num, mask, count)
        
        num = mask = count = 0
        for i in range(n-1, 0, -1):
            binary = 1 << (ord(s[i]) - 97)
            if not (mask & binary):
                count += 1
                if count<=k:
                    mask |= binary
                else:
                    num += 1
                    mask = binary
                    count = 1
            right_partition[i-1] = (num, mask, count)

        ans = 0
        for i in range(n):
            curr_seg = left_partition[i][0] + right_partition[i][0] + 2
            tot_mask = left_partition[i][1] | right_partition[i][1]
            tot_count = bin(tot_mask).count("1")
            
            if left_partition[i][2] == k and right_partition[i][2] == k and tot_count < 26:
                curr_seg += 1
            elif min(tot_count+1, 26)<=k:
                curr_seg -= 1

            ans = max(ans, curr_seg)
        
        return ans
