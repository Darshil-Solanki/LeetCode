class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        people_at_day = [0]*(forget+1)
        people_at_day[1], MOD = 1, 1_000_000_007

        for day in range(2, n+1):
            for d in range(forget-1, delay-1, -1):
                people_at_day[0] += people_at_day[d]
                people_at_day[d+1] = people_at_day[d]
            for d in range(delay-1, -1, -1):
                people_at_day[d+1] = people_at_day[d]
            people_at_day[0] = 0

        return sum(people_at_day)%MOD
