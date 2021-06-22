from resources_report import resources

bank = round(0, 2)


def report_resources():
    """This checks the resources left in the machine"""
    global bank
    water = resources["water"]
    milk = resources["milk"]
    coffee = resources["coffee"]
    report = f"Water: {water}ml \nMilk: {milk}ml \nCoffee: {coffee}g \nMoney: £{bank}"
    return report


def check_resources(water, milk, coffee):
    # How could I make the following a for loop?
    if water > resources["water"]:
        print("Sorry, there is not enough water.")
        return "no resources"
    elif milk > resources["milk"]:
        print("Sorry, there is not enough milk.")
        return "no resources"
    elif coffee > resources["coffee"]:
        print("Sorry, there is not enough coffee.")
        return "no resources"


def process_coins(price):
    """Checks what the user has inputted, if not enough, rejected, if enough, calculates and returns change"""
    global bank
    quarters = float(input("How many quarters? "))
    dimes = float(input("How many dimes? "))
    nickles = float(input("How many nickles? "))
    pennies = float(input("How many pennies? "))
    value_calculation = (0.25 * quarters) + (0.10 * dimes) + (0.05 * nickles) + (0.01 * pennies)
    if value_calculation < price:
        print("Sorry, that's not enough money. Money refunded.")
        main()
    elif value_calculation > price:
        change = round(value_calculation - price, 2)
        print(f"Here is ${change} dollars in change.")
        bank += price


def make_espresso():
    if check_resources(50, 0, 18) == "no resources":
        main()
    process_coins(1.5)
    print("Enjoy your espresso, have a nice day.")
    resources["water"] = resources["water"] - 50
    resources["milk"] -= 0
    resources["coffee"] -= 18


def make_latte():
    if check_resources(200, 150, 24) == "no resources":
        main()
    process_coins(2.5)
    print("Enjoy your latte, have a nice day.")
    resources["water"] -= 200
    resources["milk"] -= 150
    resources["coffee"] -= 24


def make_cappuccino():
    if check_resources(250, 100, 24) == "no resources":
        main()
    process_coins(3.0)
    print("Enjoy your cappuccino, have a nice day.")
    resources["water"] -= 250
    resources["milk"] -= 100
    resources["coffee"] -= 24


machine_off = False


def main():
    global machine_off
    choice = input("What would you like? (espresso / latte / cappuccino?) ")
    if choice == "espresso":
        make_espresso()
    elif choice == "latte":
        make_latte()
    elif choice == "cappuccino":
        make_cappuccino()
    elif choice == "report":
        print(report_resources())
    elif choice == "off":
        machine_off = True
    else:
        print("Invalid entry.")


while not machine_off:
    main()
