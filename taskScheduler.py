class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        c = Counter(tasks)
        hold = []

        ans  = 0
        while c or hold:
            ans += 1
            if c:
                task, count = c.most_common(1)[0]
                c.pop(task)
                count-=1
                if count>0:
                    hold.append([task, count, n+1])
            
            temp = []
            for i in range(len(hold)):
                hold[i][2]-=1
                if not hold[i][2]:
                    temp.append(hold[i])
            
            for t, cnt, _ in temp:
                c[t]=cnt
            
            hold = [h for h in hold if h[2] ]

        return ans


        # mathematical answer from editorial
        # c = Counter(tasks)
        # _, maxCount = c.most_common(1)[0]
        # maxt = sum(1 for _, cnt in c.items() if cnt==maxCount)
        # return max((maxCount-1)*(n+1)+maxt, len(tasks))
