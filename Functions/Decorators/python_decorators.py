# simple decorator example
def simple_decorator(func):
    def wrapper():
        print('Before function call')
        func()
        print('After function call')
    return wrapper


def say_hello():
    print('Hello Python!')


if __name__ == "__main__":
    say_hello = simple_decorator(say_hello)
    print(say_hello)
    say_hello()
