class Solution:
    def minTime(self, skill: List[int], mana: List[int]) -> int:
        skill_tot, n = sum(skill), len(skill)
        end_times = [0]*n

        for potion in mana:
            curr_time = end_times[0]

            for i, w_skill in enumerate(skill):
                curr_time = max(curr_time, end_times[i]) + w_skill*potion
                
            end_times[n-1] = curr_time
            for i in range(n-2, -1, -1):
                end_times[i] = end_times[i+1] - skill[i+1]*potion
        
        return end_times[n-1]
