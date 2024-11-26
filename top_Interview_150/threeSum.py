class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res=[]
        seen = set()
        for i,val in enumerate(nums):
            if i>0 and val==nums[i-1]:
                continue
            l=i+1
            r=n-1
            while l<r:
                curr = nums[l]+nums[r]
                if curr==-val:
                    triplet  = (nums[l],val,nums[r])
                    if triplet not in seen:
                        res.append([nums[l],val,nums[r]])
                        seen.add(triplet)
                if curr<-val:
                    l+=1
                else:
                    r-=1
        return res
