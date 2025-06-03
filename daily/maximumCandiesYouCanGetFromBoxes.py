class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        candy = 0
        queue = deque(initialBoxes)

        while queue:
            n = len(queue)
            temp = 0
            for _ in range(len(queue)):
                curr_box = queue.popleft()
                if status[curr_box]:
                    candy += candies[curr_box]
                else:
                    queue.append(curr_box)
                    temp += 1
                    continue
                for box_key in keys[curr_box]:
                    status[box_key] = 1
                for box in containedBoxes[curr_box]:
                    queue.append(box)
            if temp == n:
                break

        
        return candy
