import random


############DEBUGGING#####################

# 1. Describe Problem
def my_function():
    # for i in range(1, 20): <-- cause error
    for i in range(1, 21):
        if i == 20:
            print("You got it")


my_function()

# 2. Reproduce the Bug
# from random import randint
dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
# dice_num = randint(1, 6) <-- cause error
dice_num = random.randint(0, 5)
print(dice_imgs[dice_num])

# 3. Play Computer
year = int(input("What's your year of birth?"))
if year > 1980 and year < 1994:
    print("You are a millenial.")
# elif year > 1994: <-- cause error
elif year >= 1994:
    print("You are a Gen Z.")

# 4. Fix the Errors
# age = input("How old are you?") <-- cause error
age = int(input("How old are you?"))
if age > 18:
    # print("You can drive at age {age}.") <-- cause error
    print(f"You can drive at age {age}.")

# 5. Print is Your Friend
pages = 0
word_per_page = 0
pages = int(input("Number of pages: "))
# word_per_page == int(input("Number of words per page: ")) <-- cause don't work expected
word_per_page = int(input("Number of words per page: "))
print(f"pages = {pages}")
print(f"word_per_page = {word_per_page}")
total_words = pages * word_per_page
print(total_words)


# 6. Use a Debugger
def mutate(a_list):
    b_list = []
    for item in a_list:
        new_item = item * 2
        b_list.append(new_item)
    # b_list.append(new_item) <-- don't work expected
    print(b_list)


mutate([1, 2, 3, 5, 8, 13])

# 7. Take a Break
# 8. Ask a Friend
# 9. Run Code Often - Build Small to Large
# 10. Ask StckOverflow(https://stackoverflow.com/)