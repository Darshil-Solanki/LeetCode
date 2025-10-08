class Solution:
    def successfulPairs(
        self, spells: List[int], potions: List[int], success: int
    ) -> List[int]:
        potions.sort()
        n = len(potions)
        ans = []
        for spell in spells:
            left, right = 0, n - 1
            while left <= right:
                mid = (left + right) // 2
                if spell * potions[mid] >= success:
                    right = mid - 1
                else:
                    left = mid + 1
            ans.append(n - left)
        return ans

        # similar approach using math to find min require and built in method to binary search leads faster approach
        # potions.sort()
        # n = len(potions)
        # result = []

        # for spell in spells:
        #     min_needed = ceil(success/spell) #( success + spell - 1 ) // spell  # Equivalent to ceil(success / spell)
        #     index = bisect_left(potions, min_needed)
        #     result.append(n - index)  # All potions from index to end are valid
        # return result

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
