class Solution:
    def rotateElements(self, nums: List[int], k: int) -> List[int]:
        if k==0: return nums
        idxs = []
        for i, num in enumerate(nums):
            if num<0:
                continue
            idxs.append((i, num))

        n = len(idxs)
        if n<2: return nums
        rotate = k%n

        for i, (idx, num) in enumerate(idxs):
            new_idx = i-rotate
            old_idx, _ = idxs[new_idx]
            nums[old_idx] = num

        return nums
                
            
        
