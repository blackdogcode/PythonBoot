# 클래스 안에 정의할 수 있는 빌트 인 메소드

# 모든 데이터 타입은 클래스
print(int)
print(list)
print(dict)
print(set)

# 클래스의 모든 속성 및 메소드 출력
print(dir(int))
print(dir(list))

# 빌트인 메소드를 이용
i = 10
print(i.__add__(100))
print(i.__bool__(), bool(i))
print(i.__mul__(7), i * 7)


# 클래스 예제 1
class Fruit:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name} is ${self.price}"

    def __add__(self, other):
        return self.price + other.price

    def __sub__(self, other):
        return self.price - other.price

    def __le__(self, other):
        if self.price <= other.price:
            return True
        else:
            return False

    def __ge__(self, other):
        if self.price >= other.price:
            return True
        else:
            return False


f1 = Fruit("apple", 10)
f2 = Fruit("orange", 5)
print(f1)
print(f2)

print(f1 + f2)
print(f1 - f2)
print(f1 >= f2)
print(f1 <= f2)
