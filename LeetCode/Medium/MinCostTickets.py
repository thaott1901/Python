from typing import List

class Tickets:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        lastDay = days[-1]
        dp = [0] * (lastDay + 1)
        for i in range(1, lastDay + 1):
            if i not in days:
                dp[i] = dp[i - 1]
            else:
                dp[i] = min(
                    dp[max(0, i - 1)] + costs[0],
                    dp[max(0, i - 7)] + costs[1],
                    dp[max(0, i - 30)] + costs[2]
                )
        return dp[-1]
        
ticket = Tickets()
days = [1,4,6,7,8,20]
costs = [2, 7, 15]
min_cost = ticket.mincostTickets(days, costs)
print(min_cost)