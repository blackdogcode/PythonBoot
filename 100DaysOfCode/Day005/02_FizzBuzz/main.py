def divisible_3(number):
    total = 0
    while number != 0:
        total += int(number % 10)
        number = int(number / 10)
    return total % 3 == 0


def divisible_5(number):
    number = int(number % 10)
    return number == 0 or number == 5


if __name__ == "__main__":
    for num in range(1, 16):
        if divisible_3(num):
            if divisible_5(num):
                print('FizzBuzz')
            else:
                print('Fizz')
        elif divisible_5(num):
            if divisible_3(num):
                print('FizzBuzz')
            else:
                print('Buzz')
        else:
            print(f'{num}')
