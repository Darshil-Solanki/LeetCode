class Solution:
    def minimumPushes(self, word: str) -> int:
        cnt = Counter(word)
        i = 0
        cost = {}
        for c, _ in cnt.most_common():
            if i<8:
                curr_cost = 1
            elif i<16:
                curr_cost = 2
            elif i<24:
                curr_cost = 3
            else:
                curr_cost = 4
            cost[c] = curr_cost
            i += 1
        
        return sum(cost[c]*no for c, no in cnt.items())
