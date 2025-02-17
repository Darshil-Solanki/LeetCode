class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        n = len(tiles)
        hashmap = defaultdict(str)
        seen = [False]*n

        def backtrack(curr):
            hashmap[curr] = True
            
            for i in range(n):
                if not seen[i]:
                    seen[i]=True
                    backtrack(curr+tiles[i])
                    seen[i]=False

        backtrack("")
        return len(hashmap)-1
    
    # No need to store all permutation using character counter
    # def numTilePossibilities(self, tiles: str) -> int:  
    #     n = len(tiles)
    #     tile_counts = Counter(tiles)
    #     self.ans = 0

    #     def backtrack(curr):
    #         if curr:
    #             self.ans += 1  

    #         for tile, count in tile_counts.items():
    #             if count > 0:  
    #                 tile_counts[tile] -= 1  
    #                 backtrack(curr + tile)  
    #                 tile_counts[tile] += 1  

    #     backtrack("")
    #     return self.ans
