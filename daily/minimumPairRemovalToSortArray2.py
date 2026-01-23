class Node:
    def __init__(self, value, left):
        self.value = value
        self.left = left
        self.prev = None
        self.next = None

class PQItem:
    def __init__(self, first, second, cost):
        self.first, self.second, self.cost = first, second, cost

    def __lt__(self, other):
        if self.cost == other.cost:
            return self.first.left<other.first.left
        return self.cost<other.cost

class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        pq = []
        head = Node(nums[0], 0)
        curr = head
        merged = [False]*len(nums)
        decrease_cnt = 0
        count = 0

        for i in range(1, len(nums)):
            new_node = Node(nums[i], i)
            curr.next = new_node
            new_node.prev = curr
            pq.append(PQItem(curr, new_node, curr.value+new_node.value))

            if nums[i-1]>nums[i]:
                decrease_cnt += 1
            
            curr = new_node
        
        heapify(pq)

        while decrease_cnt > 0:
            item = heappop(pq)
            first, second, cost = item.first, item.second, item.cost
            if (merged[first.left] or merged[second.left] or first.value+second.value!=cost):
                continue

            count += 1
            
            if first.value > second.value:
                decrease_cnt -= 1
                
            prev_node = first.prev
            next_node = second.next
            first.next = next_node
            if next_node:
                next_node.prev = first
            
            if prev_node:
                if prev_node.value > first.value and prev_node.value<=cost:
                    decrease_cnt -= 1
                elif prev_node.value <= first.value and prev_node.value>cost:
                    decrease_cnt += 1
                heappush(pq, PQItem(prev_node, first, prev_node.value+cost))
            if next_node:
                if second.value>next_node.value and cost<=next_node.value:
                    decrease_cnt -= 1
                elif second.value<=next_node.value and cost>next_node.value:
                    decrease_cnt += 1
                heappush(pq, PQItem(first, next_node, cost+next_node.value))
            first.value = cost
            merged[second.left] = True
        
        return count
            
        
