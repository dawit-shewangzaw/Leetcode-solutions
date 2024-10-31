class Solution:
    def minimumTotalDistance(self, robot, factory):
        # Sort robots and factories by position for optimal pairing
        robot.sort()
        factory.sort()

        n = len(robot)
        m = len(factory)

        # Initialize a DP table where dp[i][j] is the minimum distance for the first i robots with j factories considered
        dp = [[float('inf')] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = 0  # Zero distance if no robots and no factories are involved

        # Process each factory
        for i in range(1, m + 1):
            factoryPos = factory[i - 1][0]
            limit = factory[i - 1][1]

            for j in range(n + 1):
                dp[i][j] = dp[i - 1][j]  # Case where we don't use this factory

                totalDistance = 0
                # Check combinations by assigning up to `limit` robots to the factory
                for k in range(1, min(j, limit) + 1):
                    totalDistance += abs(robot[j - k] - factoryPos)
                    if dp[i - 1][j - k] != float('inf'):
                        dp[i][j] = min(dp[i][j], dp[i - 1][j - k] + totalDistance)

        return dp[m][n]  # Minimum total distance to repair all robots with all factories considered
