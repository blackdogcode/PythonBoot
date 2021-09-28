# https://algospot.com/judge/problem/read/FESTIVAL
import sys
input = sys.stdin.readline


def festival(n, l, costs):
    min_average_cost = float('+inf')
    for days in range(l, n + 1):
        for start_of_day in range(0, n - days):
            average_cost = sum(costs[start_of_day:start_of_day + days]) / days
            if average_cost < min_average_cost:
                min_average_cost = average_cost
    return min_average_cost


test_case = int(input())
for _ in range(test_case):
    N, L = map(int, input().split())
    daily_costs = list(map(int, input().split()))
    min_cost = festival(N, L, daily_costs)
    print(min_cost)



