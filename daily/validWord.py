class Solution:
    def isValid(self, word: str) -> bool:
        pattern = r'^(?=[A-Za-z0-9]{3,}$)(?=.*[AEIOUaeiou])(?=.*[B-DF-HJ-NP-TV-Zb-df-hj-np-tv-z])[A-Za-z0-9]+$'
        return re.match(pattern, word) is not None
