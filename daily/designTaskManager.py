class TaskManager:

    def __init__(self, tasks: List[List[int]]):
        self.task_priority = defaultdict(int)
        self.task_to_user = defaultdict(int)
        self.task_heap = []
        for user, task, pri in tasks:
            self.task_priority[task] = -pri
            self.task_heap.append(((-pri, -task), user))
            self.task_to_user[task] = user

        heapify(self.task_heap)

    def add(self, userId: int, taskId: int, priority: int) -> None:
        self.task_priority[taskId] = -priority
        heappush(self.task_heap,((-priority, -taskId), userId))
        self.task_to_user[taskId] = userId
        

    def edit(self, taskId: int, newPriority: int) -> None:
        self.task_priority[taskId] = -newPriority
        heappush(self.task_heap, ((-newPriority, -taskId), self.task_to_user[taskId]))

    def rmv(self, taskId: int) -> None:
        self.task_priority[taskId] = -1
        del self.task_to_user[taskId]

    def execTop(self) -> int:
        while self.task_heap and (self.task_heap[0][0][0]!=self.task_priority[-self.task_heap[0][0][1]] or self.task_heap[0][1]!=self.task_to_user[-self.task_heap[0][0][1]]):
            heappop(self.task_heap)
        if not self.task_heap:
            return -1
        
        (_, task), user = heappop(self.task_heap)
        self.task_priority[-task] = -1
        del self.task_to_user[-task]
        return user


# Your TaskManager object will be instantiated and called as such:
# obj = TaskManager(tasks)
# obj.add(userId,taskId,priority)
# obj.edit(taskId,newPriority)
# obj.rmv(taskId)
# param_4 = obj.execTop()
