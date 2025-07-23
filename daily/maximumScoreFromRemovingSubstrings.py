class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        total_score = 0
        high_pri_pair = "ab" if x>y else "ba"
        low_pri_pair = "ab" if high_pri_pair=="ba" else "ba"

        def remove_substr(s, pair):
            stack = []
            for c in s:
                if (stack and stack[-1] == pair[0] and c==pair[1]):
                    stack.pop()
                else:
                    stack.append(c)
            return "".join(stack)

        # remove high_pri first
        string_after_first_removal = remove_substr(s, high_pri_pair)
        removed_pairs_count = (len(s)-len(string_after_first_removal))//2

        total_score += removed_pairs_count * max(x, y)

        # remove low_pri
        string_after_second_removal = remove_substr(string_after_first_removal, low_pri_pair)
        removed_pairs_count = (len(string_after_first_removal)-len(string_after_second_removal))//2

        total_score += removed_pairs_count * min(x, y)

        return total_score
