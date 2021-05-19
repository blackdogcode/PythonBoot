def cube(x):
    return x ** 3


def greet(name):
    print(f'Hello {name}!')


if __name__ == "__main__":
    x, y, z = 1, 2, 3
    print(f'cube({x}) = {cube(x)}')
    print(f'cube({y}) = {cube(y)}')
    print(f'cube({z}) = {cube(z)}')

    greet('IoTex')

