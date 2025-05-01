class Solution:
    def maxTaskAssign(self, tasks: List[int], workers: List[int], pills: int, strength: int) -> int:
        n, m = len(tasks), len(workers)
        tasks.sort()
        workers.sort()

        def check(k):
            curr_p = pills
            w = workers[m-k:]
            for i in range(k-1, -1, -1):
                if w[-1]>=tasks[i]:
                    w.pop()
                else:
                    if not curr_p: return False
                    pos = bisect_left(w, tasks[i]-strength) # pos of worker with strength tasks[i]-strength(of pill)
                    if pos==len(w): return False
                    curr_p -= 1
                    w.pop(pos)
            return True
        
        left, right, ans = 1, min(m, n), 0
        while left <= right:
            mid = (left+right)//2
            if check(mid):
                ans = mid
                left = mid+1
            else:
                right = mid-1
        
        return ans
