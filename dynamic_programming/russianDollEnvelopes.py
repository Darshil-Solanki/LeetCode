class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes.sort(key = lambda x: (x[0], -x[1]))
        lis = []

        for w, h in envelopes:
            pos = bisect_left(lis,h)
            if pos==len(lis):
                lis.append(h)
            else:
                lis[pos] = h
            
        return len(lis)

        # reduce Runtime one because of finding pos only for element inside array and another major effect due to sorting in different sort method for both width and height 
        # envelopes.sort(key = lambda x: -x[1])
        # envelopes.sort(key = lambda x: x[0])
        
        # lis = [envelopes[0][1]]

        # for w, h in envelopes:
        #     if lis[-1]<h:
        #         lis.append(h)
        #     else:
        #         pos = bisect_left(lis,h)
        #         lis[pos] = h
            
        # return len(lis)
