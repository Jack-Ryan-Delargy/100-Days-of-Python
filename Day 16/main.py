from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# Create objects
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

is_on = True

while is_on:
    # Get available drinks from menu
    options = menu.get_items()
    choice = input(f"What would you like? ({options}): ")
    
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        # Find the drink
        drink = menu.find_drink(choice)
        
        # Check if drink exists and resources are sufficient
        if drink and coffee_maker.is_resource_sufficient(drink):
            # Process payment
            if money_machine.make_payment(drink.cost):
                # Make the coffee
                coffee_maker.make_coffee(drink)