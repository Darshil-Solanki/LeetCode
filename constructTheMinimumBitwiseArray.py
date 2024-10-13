class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        res = []
        hashMap = {}
        for n in nums:
            for i in range(n):
                if i in hashMap:
                    if i+1 in hashMap:
                        if hashMap[i]|hashMap[i+1]==n:
                            res.append(hashMap[i])
                            break
                    else:
                        hashMap[i+1]= (i+1) | (i+2)
                        if hashMap[i]|hashMap[i+1]==n:
                            res.append(hashMap[i])
                            break
                else:
                    hashMap[i] = i|(i+1)
                    hashMap[i+1] = (i+1) | (i+2)
                    if hashMap[i]|hashMap[i+1]==n:
                            res.append(hashMap[i])
                            break
            else:
                if n-1 | n == n:
                    res.append(n-1)
                else:
                    res.append(-1) 
        return res
