class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        res = []
        code_pattern = r"^[a-zA-Z0-9_]+$"
        valid_b = set(["electronics", "grocery", "pharmacy", "restaurant"])
        
        for c, b, flag in zip(code, businessLine, isActive):
            if flag and re.match(code_pattern, c) and b in valid_b:
                res.append((b, c))

        res.sort()
        return [c for b, c in res]                
