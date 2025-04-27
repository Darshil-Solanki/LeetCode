class Solution:
    def findCommonResponse(self, responses: List[List[str]]) -> str:
        count = defaultdict(int)
        maxCount = 0
        for response in responses:
            for ans in set(response):
                count[ans]+=1
                if count[ans]>maxCount: maxCount = count[ans]

        l = [value for value, cnt in count.items() if cnt==maxCount]
        l.sort()
        return l[0]
