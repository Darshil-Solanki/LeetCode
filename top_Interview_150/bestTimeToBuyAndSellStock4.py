class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        after = [[0]*(k+1) for i in range(2)]
        curr = [[0]*(k+1) for i in range(2)]
        for i in range(n-1, -1, -1):
            for buy in range(2):
                for cap in range(k):
                    if buy:
                        curr[buy][cap] = max( -prices[i]+after[0][cap], after[1][cap])
                    else:
                        curr[buy][cap] =  max(prices[i]+after[1][cap-1], after[0][cap])
            after = curr
        return after[1][cap]

        # Recursive Solution
        # n = len(prices)
        # def dp(i, buy, cap):
        #     if i==n or cap==0: return 0
        #     if buy:
        #         return max(-prices[i]+dp(i+1, 0, cap), dp(i+1, 1, cap))
        #     else:
        #         return max(prices[i]+dp(i+1, 1, cap-1), dp(i+1, 0, cap))
        # return dp(0, 1, k)

# Copied from Submission having least runtime usage doubly linked list but i don't understand this !!!
# class DoubleLinkListNode:
#     def __init__(self, ind, pre = None, next = None):
#         self.ind = ind
#         self.pre = pre if pre else self
#         self.next = next if next else self
# class Solution:
#     def MinMaxList(self, arr: List[int]) -> List[int]:
#         n = len(arr)
#         if n == 0:
#             return []
#         sign = -1
#         res = [9999]
#         for num in arr:
#             if num * sign > res[-1] * sign:
#                 res[-1] = num
#             else:
#                 res.append(num)
#                 sign *= -1
#         if len(res) & 1:
#             res.pop()
#         return res
#     def maxProfit(self, k: int, prices: List[int]) -> int:
#         newP = self.MinMaxList(prices)
#         n = len(newP)
#         m = n // 2
#         res = 0
#         for i in range(m):
#             res += newP[i*2+1] - newP[i*2]
#         if m <= k:
#             return res
#         head, tail = DoubleLinkListNode(-1), DoubleLinkListNode(-1)
#         NodeList = [DoubleLinkListNode(0, head)]
#         for i in range(1, n):
#             NodeList.append(DoubleLinkListNode(i, NodeList[-1]))
#             NodeList[i-1].next = NodeList[i]
#         NodeList[n-1].next = tail
#         head.next, tail.pre = NodeList[0], NodeList[n-1]
#         heap = []
#         for i in range(n-1):
#             if i&1:
#                 heappush(heap, [newP[i] - newP[i+1], i, i+1, 0])
#             else:
#                 heappush(heap, [newP[i+1] - newP[i], i, i+1, 1])
#         while m > k:
#             loss, i, j, t = heappop(heap)
#             if NodeList[i] == None or NodeList[j] == None: continue
#             m -= 1
#             res -= loss
#             nodei, nodej = NodeList[i], NodeList[j]
#             nodel, noder = nodei.pre, nodej.next
#             l, r = nodel.ind, noder.ind
#             valL, valR = newP[l], newP[r]
#             noder.pre, nodel.next = nodel, noder
#             NodeList[i], NodeList[j] = None, None
#             if t == 0:
#                 heappush(heap, [valR - valL, l, r, 1])
#             elif l != -1 and r != -1:
#                 heappush(heap, [valL - valR, l, r, 0])
#         return res
