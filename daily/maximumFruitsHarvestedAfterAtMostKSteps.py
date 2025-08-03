class Solution:
    def maxTotalFruits(self, fruits: List[List[int]], startPos: int, k: int) -> int:
        def step(left, right):
            if fruits[right][0]<=startPos:
                return startPos-fruits[left][0]
            elif fruits[left][0]>=startPos:
                return fruits[right][0]-startPos
            else:
                return (
                    min(abs(startPos-fruits[right][0]), abs(startPos-fruits[left][0])) 
                    + fruits[right][0] - fruits[left][0]
                )
        
        left = 0
        n = len(fruits)
        tot = temp_tot = 0
        for right in range(n):
            temp_tot += fruits[right][1]
            while left<=right and step(left, right)>k:
                temp_tot -= fruits[left][1]
                left += 1

            tot = max(tot, temp_tot)
        
        return tot
