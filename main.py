import time
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0
}
separator = "--------------------------------------------------------"


def enough_resources(drink):
    coffee_needed = MENU[drink]["ingredients"]["coffee"]
    milk_needed = MENU[drink]["ingredients"]["milk"]
    water_needed = MENU[drink]["ingredients"]["water"]
    if (resources["coffee"] - coffee_needed) < 0:
        print("There is not enough coffee in the machine. Please try again later")
        return 1
    if (resources["milk"] - milk_needed) < 0:
        print("There is not enough milk in the machine. Please try again later")
        return 1
    if (resources["water"] - water_needed) < 0:
        print("There is not enough water in the machine. Please try again later")
        return 1
    return 0


def enough_money(drink):
    print("The cost of your " + drink + " is: $ " + str(MENU[drink]["cost"]) + " dollars")
    quarters = 0.25 * int(input("Type number of quarters: "))
    dimes = 0.10 * int(input("Type number of dimes: "))
    nickles = 0.05 * int(input("Type number of nickles: "))
    pennies = 0.01 * int(input("Type number of pennies: "))
    total = quarters + dimes + nickles + pennies
    print("You inserted $ " + str(total) + " dollars in coins.")
    if total < MENU[drink]["cost"]:
        print("Sorry that's not enough money. Money refunded.")
        return 1
    if total >= MENU[drink]["cost"]:
        print("Your change is $" + str(total - MENU[drink]["cost"]) + " dollars")
    print(separator)
    return 0


def make_adjustments(drink):
    coffee_needed = MENU[drink]["ingredients"]["coffee"]
    milk_needed = MENU[drink]["ingredients"]["milk"]
    water_needed = MENU[drink]["ingredients"]["water"]
    resources["coffee"] = resources["coffee"] - coffee_needed
    resources["water"] = resources["water"] - water_needed
    resources["milk"] = resources["milk"] - milk_needed
    resources["money"] = resources["money"] + MENU[drink]["cost"]
    return 0


def make_drink(drink):
    if enough_resources(drink) == 1:
        return 1
    if enough_money(drink) == 1:
        return 1
    print("We are making your " + drink + ". Please wait!")
    time.sleep(5)
    print(separator)
    make_adjustments(drink)
    print("Please remove your " + drink + " from the machine.")
    time.sleep(5)
    return 0


def generate_report():
    print("Here is the report you asked for: ")
    print("Water: " + str(resources["water"]) + " ml")
    print("Milk: " + str(resources["milk"]) + " ml")
    print("Coffee: " + str(resources["coffee"]) + " gr")
    print("Money: $" + str(resources["money"]) + " dollars")
    return 0


while 1:
    option = input("What would you like? (espresso/latte/cappuccino): ")

    if option == 'espresso' or option == 'latte' or option == 'cappuccino':
        print(separator)
        make_drink(option)
        print(separator)

    elif option == 'off':
        print(separator)
        print("Thank you for using our machine")
        exit(0)

    elif option == 'report':
        print(separator)
        generate_report()
        print(separator)

    else:
        print(separator)
        print("Please choose a valid option!")
        print(separator)
