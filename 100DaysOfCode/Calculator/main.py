import art


def add(a, b): return a + b


def subtract(a, b): return a - b


def multiply(a, b): return a * b


def divide(a, b): return a / b


calculator = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

print(art.logo)
print("Welcome to the Calculator!")
accumulator = float(input("What's the first number: "))
is_continue = True
while is_continue:
    operator = input("Enter operator: ")
    num = float(input("Enter number: "))
    accumulator = calculator[operator](accumulator, num)
    print(accumulator)
    if input("Do you want to continue calculation? (y/n): ").lower() == "n":
        is_continue = False
