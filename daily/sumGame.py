class Solution:
    def sumGame(self, num: str) -> bool:
        # copied from editorial
        n = len(num)

        def get(left=True):
            tot, q = 0, 0
            for c in (num[:n//2] if left else num[n//2:]):
                if c == "?":
                    q += 1
                else:
                    tot += int(c)
            return tot, q

        left_tot, left_q = get()
        right_tot, right_q = get(False)


        return (left_q + right_q) % 2 == 1 or left_tot - right_tot != (right_q - left_q) * 9//2
