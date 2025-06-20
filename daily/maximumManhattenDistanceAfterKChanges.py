class Solution:
    def maxDistance(self, s: str, k: int) -> int:
        north = south = east = west = 0
        ans = 0

        for d in s:
            match d:
                case "N":
                    north += 1
                case "S":
                    south += 1
                case "E":
                    east += 1
                case "W":
                    west += 1
            
            vertical = min(north, south, k) # can be changed to increase distance
            horizontal = min (east, west, k-vertical)

            ans = max(ans, abs(north-south)+ vertical*2 + abs(east-west)+ horizontal*2)
        
        return ans

       
