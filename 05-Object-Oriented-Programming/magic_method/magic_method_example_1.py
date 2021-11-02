# 클래스 예제2

class Vector:
    def __init__(self, *args):
        """
        Create a Vector
        :param args: i.g. (5, 10)
        """
        if len(args) == 0:
            self.x, self.y = 0, 0
        else:
            self.x, self.y = args

    def __repr__(self):
        """
        :return: vector information
        """
        return f"Vector({self.x}, {self.y})"

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        return Vector(self.x * other, self.y * other)

    def __bool__(self):
        """
        :return: if vector is origin
        """
        return bool(max(self.x, self.y))


# Vector 인스턴스 생성
v1 = Vector(5, 7)
v2 = Vector(23, 35)
v3 = Vector()

print(v1, v2, v3)

# 매직메소드 출력
print(Vector.__init__.__doc__)
print(Vector.__repr__.__doc__)
print(Vector.__bool__.__doc__)

print(v1 + v2)
print(v1 * 3)
print(bool(v1), bool(v2), bool(v3))
