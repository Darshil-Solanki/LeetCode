class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        
        def check(time):
            repair = 0
            for rank in range(1, max_rank+1):
                repair += freq[rank]*int(sqrt(time//rank))
            return repair>=cars

        min_rank = min(ranks)
        max_rank = max(ranks)

        freq = [0]*(max_rank+1)
        for rank in ranks:
            freq[rank]+=1

        left, right = 1, min_rank*cars*cars

        while left<=right:
            mid = (left+right)//2
            if check(mid):
                right = mid-1
            else:
                left = mid+1
        return left

        # def check(time):
        #     repair = 0
        #     for rank in ranks:
        #         repair += int(sqrt(time//rank))
        #     return repair>=cars

        # min_rank = min(ranks)

        # left, right = 1, min_rank*cars*cars

        # while left<=right:
        #     mid = (left+right)//2
        #     if check(mid):
        #         right = mid-1
        #     else:
        #         left = mid+1
        # return left
