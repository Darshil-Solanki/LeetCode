class Solution:
    def score(self, cards: List[str], x: str) -> int:
        first_match, second_match, both_match = defaultdict(int), defaultdict(int), 0
        for card in cards:
            if card[0]==x and card[1]==x:
                both_match += 1
            elif card[0]==x:
                first_match[card[1]] += 1
            elif card[1]==x:
                second_match[card[0]] += 1
            else:
                pass
        
        pairs, remaining = 0, 0
        s, m = sum(first_match.values()), max(first_match.values(), default=0)
        p1 = min(s-m, s//2)
        remaining += s-2*p1
        s, m = sum(second_match.values()), max(second_match.values(), default=0)
        p2 = min(s-m, s//2)
        remaining += s-2*p2
        pairs = p1+p2

        wildcard_pair = min(both_match, remaining)
        both_match -= wildcard_pair
        extra = min(pairs, both_match//2)
        return pairs+wildcard_pair+extra



