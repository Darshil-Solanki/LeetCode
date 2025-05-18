class Solution:
    def colorTheGrid(self, m: int, n: int) -> int:
        MOD = 1_000_000_007
        # all valid coloration schemes for a single row. The key represent mask and the value represents the ternary string of mask(stored as list)
        valid = {}

        for mask in range(3**m):
            color = []
            mm = mask
            
            for i in range(m):
                color.append(mm % 3)
                mm //=3
            
            if any(color[i]==color[i+1] for i in range(m-1)):
                continue
            
            valid[mask] = color
        
        # preprocess all (mask1, mask2) satisfying mask1 and mask2 when adjacent rows, the colors of the two cells in the same column are different
        adjacent = defaultdict(list)
        for mask1, color1 in valid.items():
            for mask2, color2 in valid.items():
                if mask1==mask2: continue
                if not any(x == y for x, y in zip(color1, color2)):
                    adjacent[mask1].append(mask2)

        f = [int(mask in valid) for mask in range(3**m)]
        for i in range(1, n):
            g = [0]*(3**m)
            for mask2 in valid.keys():
                for mask1 in adjacent[mask2]:
                    g[mask2] += f[mask1]
                    g[mask2] %= MOD
            f = g
        
        return sum(f) % MOD
