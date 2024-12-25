class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        res1, res2 = [], []
        nd1  = defaultdict(int)
        for i, n in enumerate(nums1):
            if n not in nd1:
                nd1[n] = 0
        nd2  = defaultdict(int)
        for i, n in enumerate(nums2):
            if n not in nd2:
                nd2[n] = 0
        for k, v in nd1.items():
            if k not in nd2:
                res1.append(k)
        for k, v in nd2.items():
            if k not in nd1:
                res2.append(k)
        return [res1, res2]

        # faster version without hashmap
        # result = [[], []]
        # set1 = set(nums1)
        # set2 = set(nums2)
        # for i in set1:
        #     if i not in set2:
        #         result[0].append(i)
        # for j in set2:
        #     if j not in set1:
        #         result[1].append(j)
        
        # return result
