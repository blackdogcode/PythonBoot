import art

def addition(a, b): return a+b
def subtract(a, b): return a-b
def multiply(a, b): return a*b
def division(a, b): return a/b

def calculator(operation, a, b):
    calc = {
        '+': addition,
        '-': subtract,
        '*': multiply,
        '/': division
    }
    return calc[operation](a, b)

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
