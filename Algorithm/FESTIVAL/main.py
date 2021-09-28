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
        if min_cost > sum_cost / days:
            min_cost = sum_cost / days
        for j in range(L + i, N):
            days += 1
            sum_cost += daily_cost[j]
            if min_cost > sum_cost / days:
                min_cost = sum_cost / days

    print("%.8f" % min_cost)
