class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        temp =[]
        if len(nums)==0:
            return []
        start=end=nums[0]
        prev=nums[0]
        for i in nums:
            if i>prev+1:
                temp.append(str(start) if start==end else f"{start}->{end}")
                start = end = i
            else:
                end=i
            prev=i
        else:
            temp.append(str(start) if start==end else f"{start}->{end}")
        return temp
