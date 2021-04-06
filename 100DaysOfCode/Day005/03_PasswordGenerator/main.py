# Password Generator ref: https://passwordsgenerator.net/
# for-loop ref: https://realpython.com/python-for-loop/
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
           'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
           'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
           'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
           'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


if __name__ == "__main__":
    print("Welcome to the PyPassword Generator!")
    cnt_letters = int(input("How many letters would you like in your password?\n--> "))
    cnt_symbols = int(input(f"How many symbols would you like?\n--> "))
    cnt_numbers = int(input(f"How many numbers would you like?\n--> "))

    password = []

    random.seed()
    for i in range(0, cnt_letters):
        password.append(random.choice(letters))
    for j in range(0, cnt_symbols):
        password.append(random.choice(symbols))
    for k in range(0, cnt_numbers):
        password.append(random.choice(numbers))
    cnt_shuffle = random.randint(1, 100)
    for m in range(0, cnt_shuffle):
        random.shuffle(password)

    print("".join(password))