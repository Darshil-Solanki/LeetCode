class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        farthest_idx = defaultdict(int)
        for i, c in enumerate(s):
            farthest_idx[c]=i
        
        result = []
        i = 0
        while i<len(s):
            prev_far = curr_far = farthest_idx[s[i]]
            for j in range(i+1, curr_far+1):
                if farthest_idx[s[j]]>curr_far:
                    curr_far = farthest_idx[s[j]]

            while curr_far>prev_far:
                temp = curr_far
                for j in range(prev_far+1, curr_far+1):
                    if farthest_idx[s[j]]>curr_far:
                        curr_far = farthest_idx[s[j]]
                prev_far = temp

            result.append(curr_far-i+1)
            i=curr_far+1

        return result
