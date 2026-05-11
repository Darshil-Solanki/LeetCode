class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        ans = []

        for num in nums:
            if num>9:
                for digit in str(num):
                    ans.append(int(digit))
            else:
                ans.append(num)
        
        return ans
