class Car:
    """
    Car class
    Author: Song
    Date: 2021.11.01
    """
    # 클래스 변수(모든 인스턴스가 공유)
    price_per_raise = 1.0

    def __init__(self, company, details):
        self.company = company
        self.details = details

    def __str__(self):
        return f"str: {self.company} - {self.details}"

    def __repr__(self):
        return f"repr: {self.company} - {self.details}"

    # Instance Method
    def detail_info(self):
        print(f"Current ID: {id(self)}")
        print(f"Car Detail Info {self.company} {self.details.get('price')}")

    def get_price(self):
        return f"Before Car Price -> {self.company}, price: {self.details.get('price')}"

    def get_price_culc(self):
        return f"Before Car Price -> {self.company}, price: {self.details.get('price') * Car.price_per_raise}"

    @classmethod
    def raise_price(cls, per):
        if per <= 1:
            print("Please Enter above 1")
            return
        else:
            cls.price_per_raise = per
            print("Succeed! price increased!")

    @staticmethod
    def is_bmw(instance):
        if instance.company == "BMW":
            return f"OK! This Car is {instance.company}"
        else:
            return f"This Car is not BMW, it is {instance.company}"


car1 = Car("Ferrari", {"color": "white", "horsepower": 400, "price": 8000})
car2 = Car("BMW", {"color": "black", "horsepower": 270, "price": 5000})
car3 = Car("Audi", {"color": "silver", "horsepower": 300, "price": 6000})


# 가격정보(인상 전)
print(car1.get_price())
print(car2.get_price())


# 가격인상(클래스 매소드 미사용)
Car.price_per_raise = 1.4
print(car1.get_price_culc())
print(car2.get_price_culc())


# 가격인상(클래스 매소드 사용)
Car.raise_price(1.6)
print(car1.get_price_culc())
print(car2.get_price_culc())

# 자동차 제조회사 확인
print(car1.is_bmw(car1))
print(car2.is_bmw(car2))

print(Car.is_bmw(car1))
print(Car.is_bmw(car2))
