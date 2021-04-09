def is_prime_number(num):
    if num == 0:
        return False
    if num != 2 and num % 2 == 0:
        return False
    for i in range(3, num, 2):
        if num % i == 0:
            return False

    return True


if __name__ == "__main__":
    integer = int(input("Prime Number Checker\nType integer: "))
    if is_prime_number(integer):
        print(f'{integer} is prime number')
    else:
        print(f'{integer} is not prime number')
