# Day 15 of 100 Days of Code Challenge
# Digital Coffee Machine
menu = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "coffee": 24,
            "milk": 150
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "coffee": 24,
            "milk": 100
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "coffee": 100,
    "milk": 200,
    "money": 0
}
machine = True


def format_report():
    """formats the coffee machine's resources"""
    water = resources["water"]
    coffee = resources["coffee"]
    milk = resources["milk"]
    money = resources["money"]
    formatted = f"Water: {water}ml\nMilk: {milk}ml\nCoffee: {coffee}g\nMoney: ${money}"
    return formatted


def take_money(coffee):
    """evaluates money and returns change if successful, restarts program if not"""
    print("Please insert coins.")
    q = int(input("How many quarters?: "))
    d = int(input("How many dimes?: "))
    n = int(input("How many nickels?: "))
    p = int(input("How many pennies?: "))
    total = (q * .25) + (d * .1) + (n * .05) + (p * .01)
    price = menu[coffee]["cost"]

    if total >= price:
        return round(total - price, 2)
    elif total < price:
        print("Sorry, that's not enough money. Money refunded.")
        order()


def eval_resources(coffee):
    """makes coffee if machine has enough resources, informs user if not"""
    for item in menu[coffee]["ingredients"]:
        if menu[coffee]["ingredients"][item] > resources[item]:
            print(f"Sorry, there is not enough {item}.")
            order()
        else:
            make_coffee(coffee)


def make_coffee(coffee):
    """reduces ingredients needed from resources and restarts order"""
    global resources
    change = take_money(coffee)
    resources["money"] += menu[coffee]["cost"]
    for item in menu[coffee]["ingredients"]:
        resources[item] -= menu[coffee]["ingredients"][item]
    print(f"Here is ${change} in change.")
    print(f"Here is your {coffee}. Enjoy!")
    order()


def refill(ingredient, amount):
    if ingredient not in resources:
        print(f"{ingredient} is not a valid ingredient, no amount updated")
        order()
    resources[ingredient] += amount
    print("Updated amounts: ")
    print(format_report())
    order()


def order():
    global machine
    while machine:
        choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
        # options: any of the drinks, report, off, refill
        if choice == "off":
            machine = False
        elif choice == "report":
            print(format_report())
        elif choice == "refill":
            item = input("What ingredient are you refilling? ").lower()
            amt = int(input(f"How much {item} are you adding? "))
            refill(item, amt)
        else:
            eval_resources(choice)


order()
