# 일급 함수 특징
# 1. 런타임 초기화 - 실행 시점에 초기화
# 2. 함수를 변수에 할당 가능
# 3. 함수를 인수로 전달 가능
# 4. 함수를 반환 가능

def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)


# 함수는 모두 객체로 취급한다
print(factorial(5))
print(factorial)
print(type(factorial))

# 함수 변수 할당
var_func = factorial
print(var_func)
print(var_func(5))

# 함수를 인수 전달 가능
print(list(map(factorial, range(1, 6))))

# Callable : 호출 연산자 -> 메소드 형태로 호출 가능한지 확인
# 호출 확인
print(callable(factorial))


# partial 사용법 : 인수 고정 -> 콜백 함수 사용
from operator import mul
from functools import partial

print(mul(10, 10), 10 * 10)

# 인수 고정
five = partial(mul, 5)
print(five(10))
print(five(100))

# 고정 추가
six = partial(five, 6)
print(six())
