MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
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

money = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def sufficient_resources(coffee_ingredients):
    """Checks whether the machine has enough resources to make the drink. Returns True for enough, and False for not
    enough. """
    enough_ingredients = True
    for item in coffee_ingredients:
        if coffee_ingredients[item] >= resources[item]:
            print(f"Sorry, there is not enough {item}.")
            enough_ingredients = False
    return enough_ingredients


def process_money():
    """Processes inserted coins and returns the total."""
    print("Please insert coins.")
    total = int(input("How many quarters? ")) * 0.25
    total += int(input("How many dimes? ")) * 0.1
    total += int(input("How many nickels? ")) * 0.05
    total += int(input("How many pennies? ")) * 0.01
    return total


def transaction_successful(money_received, drink_cost):
    """Returns True if payment is accepted, or False if the money received is insufficient."""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global money
        money += drink_cost
        return True
    else:
        print("Sorry that's not enough. Money refunded.")
        return False


def make_coffee(drink_name, order_ingredients):
    """Deduct required ingredients from resources."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name}. Enjoy!")


coffee_machine_on = True

while coffee_machine_on:
    coffee_input = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if coffee_input == "off":
        coffee_machine_on = False

    elif coffee_input == "report":
        """Lists all resources and coins inside the coffee machine."""
        print(f'Water: {resources["water"]}ml')
        print(f'Milk: {resources["milk"]}ml')
        print(f'Coffee: {resources["coffee"]}g')
        print(f'Money: ${money}')

    else:
        drink = MENU[coffee_input]
        """Adds coffee input into a drink variable, which matches to the menu dictionary."""
        if sufficient_resources(drink["ingredients"]):
            coins_inserted = process_money()
            """Adds money total into a coins inserted variable."""
            if transaction_successful(coins_inserted, drink["cost"]):
                make_coffee(coffee_input, drink["ingredients"])
                """Creates your coffee, enjoy!"""
