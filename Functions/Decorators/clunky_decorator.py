# clunky and simple decorator
def clunky_decorator(func):
    def wrapper():
        print('Before clunky Decorator')
        func()
        print('After clunky Decorator')
    return wrapper


def say_hello():
    print('Hello Python!')


if __name__ == "__main__":
    print('-' * 50)
    say_hello = clunky_decorator(say_hello)
    print(say_hello)
    say_hello()
    print('-' * 50)
