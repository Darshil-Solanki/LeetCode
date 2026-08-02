class Solution:
    def countTasks(self, tasks: List[int], shifts: List[int]) -> List[int]:
        prefix_tasks = [0]
        for t in tasks:
            prefix_tasks.append(prefix_tasks[-1]+t)

        ans = []
        spent = 0
        n = len(tasks)
        for s in shifts:
            limit = spent + s
            if limit >= prefix_tasks[-1]:
                ans.append(0)
                spent = 0
                continue

            idx = bisect_right(prefix_tasks, limit) - 1
            ans.append(n - idx)
            spent = limit
        return ans
