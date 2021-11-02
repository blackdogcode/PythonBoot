from collections import namedtuple
from math import sqrt

# 네임드 튜플 선언 방법 1
Point = namedtuple('Point', 'x y')

pt1 = Point(1.0, 5.0)
pt2 = Point(2.5, 1.5)
print(pt1, pt2)

length = sqrt((pt1.x - pt2.x) ** 2 + (pt1.y - pt2.y) ** 2)
print(length)

# 네임드 튜플 선언 방법 2
Point = namedtuple('Point', ['x', 'y'])
pt3 = Point(x=15.0, y=25.0)
print(pt3)

# 네임드 튜플 선언 방법 3
Point = namedtuple('Point', 'x, y')
pt4 = Point(17.0, 51.0)
print(pt4)

# 네임드 튜플 선언 방법 4
Point = namedtuple('Point', 'x y x class', rename=True)
pt5 = Point(10, 20, 30, 40)
print(pt5)

# 딕셔녀러 TO 네임드 튜플
point_dict = {'x': 10, 'y': 20}
Point = namedtuple('Point', "x, y")
pt6 = Point(**point_dict)
print(pt6)

# 네임드 튜플 메소드
point_list = [52, 38]
pt7 = Point._make(point_list)
print(pt7)
print(pt7._fields)
print(pt7._asdict())

# 실습  - 교실 반 20명, 4개의 반(A, B, C, D)
numbers = [str(n) for n in range(1, 21)]
ranks = ['A', 'B', 'C', 'D']

Classes = namedtuple('Classes', ['rank', 'number'])
students = [Classes(rank, number) for rank in ranks for number in numbers]
for student in students:
    print(student)
