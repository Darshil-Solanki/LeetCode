class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for a in asteroids:
            if stack and stack[-1]>0 and a<0:
                t = stack.pop()
                while t+a<0 and stack and stack[-1]>0:
                    t = stack.pop()
                if t+a>0:
                    stack.append(t)
                elif t+a==0:
                    pass
                else:
                    stack.append(a)
            else:
                stack.append(a)
        return stack

        # Bit Shorter version
        # res = []
        # for cur in asteroids:
        #     while res and res[-1] > 0 and cur < 0:
        #         if res[-1] < -cur:
        #             res.pop()
        #             continue
        #         elif res[-1] == -cur:
        #             res.pop()
        #         break
        #     else:
        #         res.append(cur)
        # return res
