class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        # from editorial
        n = len(s)
        visited = [False]*n
        ans = s
        s = s+s
        i = 0

        while not visited[i]:
            visited[i] = True
            for j in range(10):
                k_limit = 9 if b%2 else 0
                for k in range(k_limit+1):
                    t = list(s[i:i+n])
                    for p in range(1, n, 2):
                        t[p] = str((int(t[p])+ j*a) % 10)
                    for p in range(0, n, 2):
                        t[p] = str((int(t[p]) + k*a) % 10)
                    t_str = "".join(t)
                    if t_str<ans:
                        ans = t_str
            i = (i+b)%n

        return ans
