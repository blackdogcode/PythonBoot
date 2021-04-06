# Rock Paper Scissors Association - https://www.wrpsa.com/
import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''


if __name__ == "__main__":
    rsp = {0: rock, 1: scissors, 2: paper}

    user_choice = int(input('What dou you choose? Type 0 for Rock, 1 for Scissor, 2 for paper\n--> '))
    print(rsp[user_choice])

    random.seed()
    comp_choice = random.randint(0, 2)
    print(f'Computer Choice\n{rsp[comp_choice]}')

    # Rock --> Scissor --> Paper --> Rock: Winning Circle
    if user_choice == comp_choice:
        print('You Draw')
    elif (user_choice+1 % 3) == comp_choice:
        print('You Win')
    else:
        print('You Lose')
