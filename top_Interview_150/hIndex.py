class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        n = len(citations)
        for i, val in enumerate(citations):
            if n-i <= val:
                return n-i
        return 0
    
    # Better O(n) solution Forward counting Backward checking
    # def hIndex(self, citations: List[int]) -> int:
    #     n = len(citations)
    #     temp = [0]*(n+1)
    #     for cite in citations:
    #         if cite>n:
    #             temp[n]+=1
    #         else:
    #             temp[cite]+=1
    #     total=0
    #     for i in range(n,-1,-1):
    #         total+=temp[i]
    #         if total>=i:
    #             return i
