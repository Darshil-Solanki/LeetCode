class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        c = Counter(arr)
        hashmap = {}
        for i, n in enumerate(c.values()):
            if n in hashmap:
                return False
            hashmap[n]=0
        return True
        
        # shorter version
        # cnt = Counter(arr)
        # return len(set(cnt.values())) == len(cnt.values())
