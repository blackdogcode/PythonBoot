import art


def calculator(operation, number_a, number_b):
    if operation == '+':
        return number_a + number_b
    elif operation == '-':
        return number_a - number_b
    elif operation == '*':
        return number_a * number_b
    elif operation == '/':
        return number_a / number_b
    else:
        return None


if __name__ == "__main__":
    print(art.logo)

    finished = False
    while True:
        if not finished:
            num_a = float(input(f"What's the first number?: "))
        operation = input('Pick an operation\n+\n-\n*\n/\n--> ')
        num_b = float(input(f"What's the second number?: "))

        result = calculator(operation, num_a, num_b)
        print(f'{num_a} {operation} {num_b} = {result}')

        finished = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation\n--> ")
        if finished == 'y':
            finished = True
            num_a = result
        else:
            finished = False

