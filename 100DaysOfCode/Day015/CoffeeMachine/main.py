from coffee_machine import nespresso
from coffee import coffees


def turn_on(coffee_machine):
    if not coffee_machine['status']:
        coffee_machine['status'] = True
        print(f'The coffee machine is turned on successfully')


def turn_off(coffee_machine):
    if coffee_machine['status']:
        coffee_machine['status'] = False
        print(f'The coffee machine is turned off successfully')


def insert_water(amount, coffee_machine):
    coffee_machine['water'] += amount


def insert_milk(amount, coffee_machine):
    coffee_machine['milk'] += amount


def insert_coffee(amount, coffee_machine):
    coffee_machine['coffee'] += amount


def display_status(coffee_machine):
    """display current resource status of coffee machine"""
    print(f'Water: {coffee_machine["water"]}ml')
    print(f'Milk: {coffee_machine["milk"]}ml')
    print(f'Coffee: {coffee_machine["coffee"]}g')
    print(f'Money: ${coffee_machine["money"]}')
    print(f'Status: {"On" if coffee_machine["status"] else "Off"}')


def check_resource(coffee, coffee_machine):
    sufficient = False
    if coffee['water'] > coffee_machine['water']:
        print(f'Sorry there is not enough water.')
    elif coffee['milk'] > coffee_machine['milk']:
        print(f'Sorry there is not enough milk.')
    elif coffee['coffee'] > coffee_machine['coffee']:
        print(f'Sorry there is not enough coffee.')
    else:
        sufficient = True
    return sufficient


def make_coffee(coffee, coffee_machine):
    coffee_machine['water'] -= coffee['water']
    coffee_machine['milk'] -= coffee['milk']
    coffee_machine['coffee'] -= coffee['coffee']
    coffee_machine['money'] += coffee['price']


def insert_coins(coffee, coffee_machine):
    price = coffee['price']
    print(f'The price is ${price}')
    quarters, dimes, nickles, pennies = (0, 0, 0, 0)
    quarters = int(input('Insert quarters: '))
    dimes = int(input('Insert dimes: '))
    nickels = int(input('Insert nickles: '))
    pennies = int(input('Insert pennies: '))
    money = quarters * 0.25 + dimes * 0.10 + nickels * 0.05 + pennies * 0.01

    if money >= price:
        change = money - price
        if not change == 0.0:
            print(f'Here is the change ${change}')
        return True
    else:
        print(f"Sorry that's not enough money. Money refunded.")
        return False


if __name__ == "__main__":
    machine = nespresso
    turn_on(machine)

    while machine['status']:
        command = input("What would you like? (espresso/latte/cappuccino)\n--> ")
        if command in coffees.keys():
            choice = command
            if check_resource(coffees[choice], machine):
                if insert_coins(coffees[choice], machine):
                    make_coffee(coffees[choice], machine)
                    print(f'Here is your {choice}. Enjoy!')
        elif command == 'report':
            display_status(machine)
        elif command == 'off':
            turn_off(machine)
            break
        else:
            pass
