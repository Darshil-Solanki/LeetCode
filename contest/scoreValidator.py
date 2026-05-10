class Solution:
    def scoreValidator(self, events: list[str]) -> list[int]:
        score, count = 0, 0
        for event in events:
            if count==10:
                break
            match event:
                case "WD" | "NB":
                    score += 1
                case "W":
                    count += 1
                case _:
                    score += int(event)
                    
        return [score, count]
