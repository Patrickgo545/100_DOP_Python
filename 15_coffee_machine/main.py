import menu
import sys

power_status_on = True

# TODO: 2. Turn off the Coffee Machine by entering “off” to the prompt.
def off():
    global power_status_on
    print("Powering Down.")
    power_status_on = False


# TODO: 3. Print report.
def report():
    water = menu.resources["water"]
    milk = menu.resources["milk"]
    coffee = menu.resources["coffee"]

    print(f"Remaining Resources:\nWater: {water}ml \nMilk: {milk}ml \nCoffee: {coffee}g")


# TODO: 4. Check resources sufficient?
def check_resources():
    water = 0
    milk = 0
    coffee = 0

    if user_input == 'espresso':
         water = menu.MENU['espresso']['ingredients']['water']
         # milk = menu.MENU['espresso']['ingredients']['milk']
         coffee = menu.MENU['espresso']['ingredients']['coffee']

    else:
        for key in menu.MENU:
            if user_input == key:
                water = menu.MENU[key]['ingredients']['water']
                milk = menu.MENU[key]['ingredients']['milk']
                coffee = menu.MENU[key]['ingredients']['coffee']

    r_water = menu.resources['water']
    r_milk = menu.resources['milk']
    r_coffee = menu.resources['coffee']

    if water > r_water:
        print('not enough water.')
        sys.exit()
    elif milk > r_milk:
        print('Not enough milk.')
        sys.exit()
    elif coffee > r_coffee:
        print('Not enough coffee.')
        sys.exit()  


# TODO: 5. Process coins.
coin_list = ["quarter" , "dime" , "nickel" , "penny"]

coin_dictionary = {
    "quarter" : .25,
    "dime" : .1,
    "nickel" : .05,
    "penny" : .01,
}

coins_inserted = {}

def process_coins():

    for coin in coin_list:
        coin_qty = int(input(f"how many {coin}'s are you inserting: "))
        coins_inserted[coin] = coin_qty

    tender_amount = 0

    for coin in coins_inserted:
        tender_amount += coins_inserted[coin] * coin_dictionary[coin]

    return tender_amount

# TODO: 7. Make Coffee.
def make_coffee():
    # REMOVE RESOURCES
    for key in menu.MENU[user_input]["ingredients"]:
        reserves_value = menu.resources[key]
        resources_used = menu.MENU[user_input]["ingredients"][key]
        resources_left = reserves_value - resources_used

        menu.resources[key] = resources_left
        # print(resources_left)
        # print(menu.resources)

        # print(menu.MENU[user_input]["ingredients"][key])
    
    print("Dispensing Coffee, Enjoy!")
    report()
    print(f"Money: {tender_amount:.2f}")



# TODO: 1. Prompt user by asking “What would you like? (espresso/latte/cappuccino):”
while power_status_on == True:

    user_input = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if user_input =="off":
        off()

    if user_input == "report":
        report()

    for key in menu.MENU:
        if user_input == key:
            check_resources() 


# TODO: 6. Check transaction successful?
    item_cost = menu.MENU[user_input]["cost"]
    tender_amount = process_coins()
    refund_amt = item_cost - tender_amount

    if tender_amount < item_cost:
        print(f"Sorry, that's not enough. ${refund_amt:.2f} refunded.")

    elif tender_amount == item_cost:
        print('Making Coffee')

    else: 
        print(f"Making Coffee")
        print(f"amount refunded: {refund_amt:.2f}")

    make_coffee()