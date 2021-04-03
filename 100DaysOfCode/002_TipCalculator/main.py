# Rounding Strategy Reference: https://realpython.com/python-rounding/

if __name__ == '__main__':
    print(f'Welcome to the tip calculator')

    total_bill = float(input(f'What was the total bill($)?: '))
    tip_percentage = float(input(f'What percentage tip would you like to give(%)? 10, 12, 15? '))
    num_of_people = float(input(f'How many people to split the bill?: '))

    bill = total_bill / num_of_people
    tip = total_bill * tip_percentage / 100 / num_of_people
    print(f'Each person should pay: ${round(bill+tip, 2)}')
