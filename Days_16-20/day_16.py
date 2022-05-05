# Day 16 of 100 Days of Code
# OOP Coffee Machine Simulator
import coffee_maker
import menu
import money_machine

the_menu = menu.Menu()
the_coffee_maker = coffee_maker.CoffeeMaker()
the_money_machine = money_machine.MoneyMachine()


def order():
    machine = True
    while machine:
        choice = input(f"What would you like? ({the_menu.get_items()}) ")
        if choice == "off":
            machine = False
        elif choice == "report":
            the_coffee_maker.report()
            the_money_machine.report()
        else:
            cust_order = the_menu.find_drink(choice)
            if cust_order is not None:
                if the_coffee_maker.is_resource_sufficient(cust_order) and \
                        the_money_machine.make_payment(cust_order.cost):
                    the_coffee_maker.make_coffee(cust_order)
            else:
                print("Please enter a valid drink")


order()
