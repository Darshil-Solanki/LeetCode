class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        ans = numBottles

        while numBottles>=numExchange:
            numBottles -= numExchange - 1
            ans += 1
            numExchange += 1
        
        return ans

        # O(1) but runtime is higher than above solution
        # b = 2 * numExchange -3
        # c = -2 * numBottles
        # delta = b*b -4*c
        # t = math.ceil((-b+sqrt(delta))/2)
        # return numBottles + t - 1
