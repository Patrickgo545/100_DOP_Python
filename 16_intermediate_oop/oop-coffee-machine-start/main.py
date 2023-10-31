from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
import sys

# CREATE OBJECTS
menu = Menu()
coffee_maker = CoffeeMaker()
# menu_item = MenuItem(water=coffee_maker.resources["water"], milk=coffee_maker.resources["milk"], )
money_machine = MoneyMachine()

# CUSTOMER INPUT
user_input = input(f"What would you like? ({menu.get_items()}): ").lower()

# OFF COMMAND
if user_input == "off":
    print("Powering down")
    sys.exit()

# PRINT REPORT
if user_input == "report":
    coffee_maker.report()
    money_machine.report()

# CHECK IF RESOURCES ARE SUFFICIENT
user_order = menu.find_drink(user_input)
# menu_item = MenuItem(menu.menu[name])
print(user_order.menu)


