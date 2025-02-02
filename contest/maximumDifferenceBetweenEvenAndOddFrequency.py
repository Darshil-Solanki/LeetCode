class Solution:
    def maxDifference(self, s: str) -> int:
        map = [0]*26
        for c in s:
            map[ord(c)-97]+=1
        odd, even = 0, float("inf")
        for freq in map:
            if freq:
                if freq%2:
                    if freq>odd: odd = freq
                else:
                    if freq<even: even = freq
        return odd-even

        # for c in s:
        #     map[c]+=1
        # even, odd = [], []
        # for c, freq in map.items():
        #     if freq%2:
        #         odd.append(freq)
        #     else:
        #         even.append(freq)
        # return max(odd)-min(even)
