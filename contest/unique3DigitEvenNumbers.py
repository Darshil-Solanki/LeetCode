class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        n = len(digits)
        even = set()
        for i in range(n):
            for j in range(n):
                if i==j: continue
                for k in range(n):
                    if k==i or k==j: continue
                    curr = digits[i]*100+digits[j]*10+digits[k]
                    if curr%2==0 and curr>99: 
                        even.add(curr)
        return len(even)
