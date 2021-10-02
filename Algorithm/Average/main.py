# https://www.acmicpc.net/problem/1546
# len 함수를 쓸 것 이므로 실질적으로 필요없음
N = int(input()) 
scores = list(map(int, input().split()))
scores.sort()
# 가장 큰 점수 값을 구한다
max_grade = scores[-1] 
# 매번 점수/M 나눗셈을 수행하여 더해주면 실수형 표현 오차가 누적된다
# 따라서 모든 점수를 더한 후 최대 점수로 나누어 준다
sum_grade = sum(scores) / max_grade * 100
avg_grade = sum_grade / len(scores)
print(avg_grade)
