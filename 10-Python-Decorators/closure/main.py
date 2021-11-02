# 클로저 기초
# 외부에서 호출 된 함수의 변수값, 상태를 복사 후 저장 -> 이후에 접근 가능

# 클래스로 구현
class Average:
    def __init__(self):
        self.series = []

    def __call__(self, v):
        self.series.append(v)
        print(f"inner >> {self.series} / {len(self.series)}")
        return sum(self.series) / len(self.series)


avg_class = Average()

# 누적
print(avg_class(10))
print(avg_class(30))
print(avg_class(50))


# 함수로 구현
def closure():
    # 클로저 영억
    series = []  # free variables

    def average(v):
        series.append(v)
        print(f"inner >> {series} / {len(series)}")
        return sum(series) / len(series)

    return average


avg_closure = closure()
print(avg_closure)
print(avg_closure(10))
print(avg_closure(30))
print(avg_closure(50))

# 함수 내부 조사
print()
print(dir(avg_closure))
print()
print(dir(avg_closure.__code__))
print()
print(avg_closure.__code__.co_freevars)
print()
print(avg_closure.__closure__[0].cell_contents)
