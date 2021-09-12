# Rounding Strategy Reference: https://realpython.com/python-rounding/

if __name__ == '__main__':
    print("Welcome to the tip calculator")

    total_bill = float(input("What was the total bill? $"))
    tip_percentage = float(input("What percentage tip would you like to give? 10, 12, 15? "))
    num_of_people = float(input("How many people to split the bill? "))

    bill_split = total_bill / num_of_people
    tip_split = total_bill * tip_percentage / 100 / num_of_people
    print(f'Each person should pay: ${round(bill_split + tip_split, 2)}')
