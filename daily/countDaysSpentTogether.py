class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        prefix_sum = [0]
        for days in month_days:
            prefix_sum.append(prefix_sum[-1]+days)
        
        def get_day_of_year(day):
            month = int(day[:2])
            date = int(day[3:])
            return prefix_sum[month-1] + date
        
        alice_sd = get_day_of_year(arriveAlice)
        alice_ed = get_day_of_year(leaveAlice)
        bob_sd = get_day_of_year(arriveBob)
        bob_ed = get_day_of_year(leaveBob)

        return max(0, min(alice_ed, bob_ed) - max(alice_sd, bob_sd) + 1)
