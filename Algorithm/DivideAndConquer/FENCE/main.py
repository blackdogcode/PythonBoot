import sys
input = sys.stdin.readline


def solve(left, right, fence):
    # 기저사례: 판자가 하나밖에 없는 경우
    if left == right:
        return fence[left]

    # 케이스 1, 2: 두 개로 나눈 각 구간 중 최대 넓이 직사각형이 있는 경우
    # 분할: 두 구간으로 분할하여 최대값을 구한다
    mid = (left + right) // 2
    ret = max(solve(left, mid, fence), solve(mid + 1, right, fence))

    # 케이스 3: 최대 넓이 직사각형이 두 구간에 걸친 경우
    lo, hi = mid, mid + 1
    height = min(fence[lo], fence[hi])
    ret = max(ret, height * 2)  # 두 구간에 하나씩 걸치 사각형

    while left < lo or hi < right:
        # 항상 높이 높은 쪽으로 직사각형을 확장한다
        if (hi < right) and (lo == left or fence[lo - 1] < fence[hi + 1]):
            hi += 1
            height = min(height, fence[hi])
        else:
            lo -= 1
            height = min(height, fence[lo])
        ret = max(ret, height * (hi - lo + 1))

    return ret


N = int(input())
fence = [0] * N
for i in range(N):
    fence[i] = int(input())
print(solve(0, len(fence) - 1, fence))
