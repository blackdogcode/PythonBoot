from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
from menu import Menu


if __name__ == '__main__':
    coffe_machine = CoffeeMaker()
    cash_machine = MoneyMachine()
    menu_list = Menu()
    while True:
        order = input(f"What would you like to drink?☕ {menu_list.get_items()}: ")
        # hide maintainers commands
        if order == "report":
            coffe_machine.report()
            cash_machine.report()
            continue
        if order == "off":
            break

        coffee = menu_list.find_drink(order)
        if coffee is None:
            continue

        if coffe_machine.is_resource_sufficient(coffee):
            if cash_machine.make_payment(coffee.cost):
                coffe_machine.make_coffee(coffee)




