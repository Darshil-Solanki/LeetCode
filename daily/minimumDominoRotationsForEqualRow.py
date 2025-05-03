class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        all = tops+bottoms
        n = len(tops)
        c = Counter(all)
        cmn_element, cmn_count = c.most_common(1)[0]
        
        if cmn_count<n: return -1
        ans = 0
        
        top_r, bottom_r = 0, 0
        for t, b in zip(tops, bottoms):
            if t != cmn_element:
                if top_r != -1:
                    top_r = top_r+1 if b==cmn_element else -1
            if b != cmn_element:
                if bottom_r != -1:
                    bottom_r = bottom_r+1 if t==cmn_element else -1
            if top_r == bottom_r ==-1: return -1

        return min(top_r, bottom_r)

    # finding most common from first top and bottom and removing max element to find minimum no of changes in n
    # def minDominoRotations(self, A, B):
    #     for x in [A[0],B[0]]:
    #         if all(x in d for d in zip(A, B)):
    #             return len(A) - max(A.count(x), B.count(x))
    #     return -1
