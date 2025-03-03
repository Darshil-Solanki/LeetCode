class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        ans = [0]*len(nums)
        left, right = 0, len(nums)-1

        for num, rnum in zip(nums, reversed(nums)):
            if num<pivot:
                ans[left]=num
                left+=1
            if rnum>pivot:
                ans[right]=rnum
                right-=1

        while left<=right:
            ans[left]=pivot
            left+=1

        return ans

        # In theory usage more memory but practically usage same memory and run faster and if you use while loop with i and j instead of num, rnum it runtime is going higher 
        # less, more = [], []
        # for i in nums:
        #     if i < pivot:
        #         less.append(i)
        #     elif i > pivot:
        #         more.append(i)
        # return less + [pivot] * (len(nums) - len(less) - len(more)) + more
