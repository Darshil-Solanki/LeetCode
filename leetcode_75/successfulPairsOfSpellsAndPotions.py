class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        n = len(potions)
        ans = []
        for spell in spells:
            left, right = 0, n-1
            while left<=right:
                mid = (left+right)//2
                if spell*potions[mid]>=success:
                    right = mid-1
                else:
                    left = mid+1 
            ans.append(n-left)
        return ans

        # fastest method from submission
        # max_potion = max(potions)
        # pref = [0] * (max_potion + 1)
        # for el in potions:
        #     pref[el] += 1
        # pref = list(reversed(list(accumulate(reversed(pref)))))
        
        # res = [0] * len(spells)
        # for i, sp in enumerate(spells):
        #     res[i] = pref[math.ceil(success / sp)] if sp * max_potion >= success else 0
        # return res
