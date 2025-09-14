class Solution:
    def minArrivalsToDiscard(self, arrivals: List[int], w: int, m: int) -> int:
        left = ans = 0
        item_counts = defaultdict(int)
        drop = [False]*len(arrivals)
        
        for right, item in enumerate(arrivals):
            if right-left+1<=w:
                if item_counts[item]<m:
                    item_counts[item]+=1
                else:
                    drop[right] = True
                    ans += 1
            else:
                if not drop[left]:
                    item_counts[arrivals[left]] -= 1
                left += 1
                if item_counts[item]<m:
                    item_counts[item]+=1
                else:
                    drop[right] = True
                    ans += 1

        return ans
