# https://programmers.co.kr/learn/courses/30/lessons/42746

def solution(numbers):
    arr = []
    for number in numbers:
        number = str(number)
        origin = number
        number *= 3
        arr.append([number, origin])
    arr.sort()
    arr.reverse()
    answer = ''
    for num, org in arr:
        answer += org
    if answer.startswith('0'):
        answer = '0'
    return answer
