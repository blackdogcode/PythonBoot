import sys
input = sys.stdin.readline

with open('test.txt', 'r') as test_input:
    test_case = int(test_input.readline())
    for _ in range(test_case):
        N, L = map(int, test_input.readline().split())
        daily_cost = list(map(int, test_input.readline().split()))
        min_cost = float('inf')
        for i in range(N - L + 1):
            days = L
            sum_cost = sum(daily_cost[i:i + L - 1])
            for j in range(L + i - 1, N):
                sum_cost += daily_cost[j]
                avg_cost = sum_cost / days
                min_cost = avg_cost if min_cost > avg_cost else min_cost
                days += 1
        print(min_cost)
