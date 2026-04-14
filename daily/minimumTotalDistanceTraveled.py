class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        robot.sort()
        factory.sort()

        factory_positions = []
        for f in factory:
            factory_positions.extend([f[0]]*f[1])
        
        robot_count, factory_count = len(robot), len(factory_positions)
        next_dp = [0]*(factory_count + 1)
        curr_dp = [0]*(factory_count + 1)

        curr_dp[factory_count] = float("inf")
        
        for i in range(robot_count-1, -1, -1):
            for j in range(factory_count-1, -1, -1):
                fix = abs(robot[i]-factory_positions[j]) + next_dp[j+1]
                not_fix = curr_dp[j+1]
                curr_dp[j] = min(fix, not_fix)

            next_dp = curr_dp[:]

        return curr_dp[0]
