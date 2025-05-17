class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        cnt = Counter(nums)

        i = 0
        color = 0
        while i<len(nums):
            if not cnt[color]:
                color += 1
                if color>2: break
                continue
            nums[i] = color
            i += 1
            cnt[color] -= 1
            
        # for k in range(j+1, len(nums)):
        #     nums[k] = 2 
        # def quick_sort(arr, low=0, high=None):
        #     if high is None:
        #         high = len(arr)-1
        #     if low<high:
        #         pivot = arr[high]
        #         i = low-1
        #         for j in range(low,high):
        #             if arr[j]<pivot:
        #                 i += 1
        #                 arr[i], arr[j] = arr[j], arr[i]
        #         arr[i+1], arr[high] = arr[high], arr[i+1]
        #         quick_sort(arr, low, i)
        #         quick_sort(arr, i+2, high)
        
        # quick_sort(nums)
