class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        n = len(nums)
        def getDominant():
            candidate, votes = -1, 0
            for n in nums:
                if not votes:
                    votes = 1
                    candidate = n
                else:
                    if n==candidate:
                        votes+=1
                    else:
                        votes-=1
            return candidate
        
        major = getDominant()
        temp_sum = 0
        left_majorcount = []
        total_majorcount = nums.count(major)
        
        for n in nums:
            if n==major:
                temp_sum+=1
            left_majorcount.append(temp_sum)
        
        
        n = len(nums)
        for i in range(n):
            if (left_majorcount[i]>((i+1)//2) and
                (total_majorcount-left_majorcount[i])>(n-i-1)//2):
                return i

        return -1
