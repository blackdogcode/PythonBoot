# https://www.acmicpc.net/problem/1920
# 이분 탐색 알고리즘
N = int(input())
numbers = list(map(int, input().split()))
M = int(input())
targets = list(map(int, input().split()))
results = [0] * M

numbers.sort()
for idx, target in enumerate(targets):
    lo, hi = (0, N - 1)
    while lo <= hi:
        mid = int((lo + hi) / 2)
        if numbers[mid] == target:
            results[idx] = 1
            break

        if target < numbers[mid]:
            hi = mid - 1
        else:
            lo = mid + 1

for ret in results:
    print(ret)
