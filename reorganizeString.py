class Solution:
    def reorganizeString(self, s: str) -> str:
        c = Counter(s)
        pq = [(-cnt, ch) for ch, cnt in c.items()]
        heapq.heapify(pq)
        ans = ""

        prev = None
        while pq or prev:
            if prev and not pq:
                return ""
            count, ch = heapq.heappop(pq)
            ans+=ch
            count+=1

            if prev:
                heapq.heappush(pq, prev)
                prev = None

            if count<0:
                prev = (count, ch)

        return ans
