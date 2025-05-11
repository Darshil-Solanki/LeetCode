class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        if len(arr)<3: return False

        first, second, third = arr[0]%2, arr[1]%2, arr[2]%2
        for i in range(len(arr)-2):
            if first and second and third: return True
            first, second, third = second, third, arr[i+2]%2 
        
        return False
