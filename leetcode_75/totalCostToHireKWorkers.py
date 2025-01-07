class Solution:
    def totalCost(self, costs: List[int], k: int, c: int) -> int:
        tot_cost = 0
        if len(costs)//2<candidates:
            heapify(costs)
            while k>0:
                tot_cost+=heappop(costs)
                k-=1
            return tot_cost
        leftHeap, rightHeap = costs[:candidates], costs[-candidates:]
        heapify(leftHeap)
        heapify(rightHeap)
        left, right = candidates, len(costs)-candidates-1
        while left<=right and k>0:
            if leftHeap[0]<=rightHeap[0]:
                tot_cost+=heapreplace(leftHeap, costs[left])
                left+=1
            else:
                tot_cost+=heapreplace(rightHeap, costs[right])
                right-=1
            k-=1
        heap = leftHeap+rightHeap
        heapify(heap)
        while k>0:
            tot_cost+=heappop(heap)
            k-=1
        return tot_cost

        # Same with better approach by 
        # n = len(costs)
        # if c * 2 + k > n:
        #     costs.sort()
        #     return sum(costs[:k])
        # cost = 0
        # left = costs[:c]
        # right = costs[n - c :]
        # heapify(left)
        # heapify(right)
        # i, j = c, n - 1 - c
        # for _ in range(k):
        #     if left[0] <= right[0]:

        #         cost += heapreplace(left, costs[i])
        #         i += 1
        #     else:
        #         cost += heapreplace(right, costs[j])
        #         j -= 1
        # return cost
