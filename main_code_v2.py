from resources_report import resources, MENU

bank = round(0, 2)


def report_resources():
    """This checks the resources left in the machine"""
    global bank
    water = resources["water"]
    milk = resources["milk"]
    coffee = resources["coffee"]
    report = f"Water: {water}ml \nMilk: {milk}ml \nCoffee: {coffee}g \nMoney: £{bank}"
    return report


def check_resources(drink):
    for item in drink["ingredients"]:
        if drink["ingredients"][item] >= resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


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


def make_drink(drink):
    if not check_resources(drink):
        main()
    process_coins(drink["cost"])
    for item in resources:
        resources[item] -= drink["ingredients"][item]


machine_off = False


def main():
    global machine_off
    choice = input("What would you like? (espresso / latte / cappuccino?) ")
    if choice == "report":
        print(report_resources())
    elif choice == "off":
        machine_off = True
    else:
        drink = MENU[choice]
        make_drink(drink)
        print(f"Enjoy your {choice}, have a nice day.")


while not machine_off:
    main()