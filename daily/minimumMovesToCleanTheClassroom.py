class Solution:
    def minMoves(self, classroom: List[str], energy: int) -> int:
        m, n = len(classroom), len(classroom[0])

        cnt = 0
        litter_id = [[0]*n for _ in range(m)]
        sx, sy = -1, -1
        for i, row in enumerate(classroom):
            for j, ch in enumerate(row):
                if ch == "S":
                    sx, sy = i, j
                elif ch == "L":
                    litter_id[i][j] = 1 << cnt
                    cnt += 1
        
        full = 1 << cnt
        best_energy = [
            [[-1 for _ in range(full)] for _ in range(n)] for _ in range(m)
        ]
        best_energy[sx][sy][0] = energy
        queue = deque([])
        queue.append((sx, sy, 0, energy, 0))

        while queue:
            x, y, mask, e, steps = queue.popleft()
            if mask == full-1:
                return steps
            if e == 0:
                continue
            for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                nx, ny = x + dx, y + dy
                if -1<nx<m and -1<ny<n and classroom[nx][ny] != "X":
                    ne = energy if classroom[nx][ny] == "R" else e-1
                    nmask = mask | litter_id[nx][ny]
                    if ne > best_energy[nx][ny][nmask]:
                        best_energy[nx][ny][nmask] = ne
                        queue.append((nx, ny, nmask, ne, steps+1))
        
        return -1
