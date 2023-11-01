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


try:
    # CREATE OBJECT - CUSTOMER'S DRINK
    customer_drink = menu.find_drink(user_input)
    
    # CHECK IF RESOURCES ARE SUFFICIENT
    sufficient_resources = coffee_maker.is_resource_sufficient(customer_drink)

    # PROCESS COINS
    print(f"${customer_drink.cost}: ")
    customer_payment = money_machine.make_payment(customer_drink.cost)

    # MAKE COFFEE   
    coffee_maker.make_coffee(customer_drink)

except:
    print('Try again')