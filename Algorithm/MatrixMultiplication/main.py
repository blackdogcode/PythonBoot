dynamic = [-1] * 1001


def multiply_way(n):
    if n == 1 or n == 2:
        return 1
    if n == 3:
        return 2
    answer = 0
    for i in range(1, n):
        answer += multiply_way(i) * multiply_way(n - i)
    return answer


def solution(n):
    return multiply_way(n) % 10007


n = int(input())
answer = solution(n)
print(answer)
