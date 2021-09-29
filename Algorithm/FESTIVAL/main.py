# https://algospot.com/judge/problem/read/FESTIVAL
import sys
input = sys.stdin.readline

test_case = int(input())
for _ in range(test_case):
    N, L = map(int, input().split())
    daily_cost = list(map(int, input().split()))

    min_cost = float('inf')
    for i in range(N - L + 1):
        days = L
        sum_cost = sum(daily_cost[i:i + L])
        min_cost = sum_cost / days if min_cost > sum_cost / days else min_cost
        for j in range(L + i, N):
            days += 1
            sum_cost += daily_cost[j]
            min_cost = sum_cost / days if min_cost > sum_cost / days else min_cost

    print("%.8f" % min_cost)
