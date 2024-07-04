class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        neg=[]
        pos=[]
        result=[]
        for i in nums:
            if(i<0):
                neg.append(i)
            else:
                pos.append(i)
        for i,j in zip(pos,neg):
            result.extend((i,j))
        return result