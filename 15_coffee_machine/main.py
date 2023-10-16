import menu

# TODO: 1. Prompt user by asking “What would you like? (espresso/latte/cappuccino):”
user_input = input("What would you like? (espresso/latte/cappuccino): ").lower()

# TODO: 2. Turn off the Coffee Machine by entering “off” to the prompt.
def off():
    print("Powering Down.")
    return

if user_input == "off":
    off()

# TODO: 3. Print report.
def report():
    print(menu.resources)

if user_input == "report":
    report()

# TODO: 4. Check resources sufficient?
# TODO: 5. Process coins.
# TODO: 6. Check transaction successful?
# TODO: 7. Make Coffee.