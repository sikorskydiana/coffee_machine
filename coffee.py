MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk": 0
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
COINS = {"quarters": 0.25, "dimes": 0.10, "nickles": 0.05, "pennies": 0.01}


resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
def is_resource_sufficient(beverage):
    if resources["water"] >= MENU[drink]["ingredients"]["water"] \
        and resources["milk"] >= MENU[drink]["ingredients"]["milk"]\
            and resources["coffee"] >= MENU[drink]["ingredients"]["coffee"]:
        resources["water"] -= MENU[drink]["ingredients"]["water"]
        resources["milk"] -= MENU[drink]["ingredients"]["milk"]
        resources["coffee"] -= MENU[drink]["ingredients"]["coffee"]
        return True
    else:
        print("Sorry, there are no sufficient ingredients ")
        return False

def calculator():
    total = quarters*COINS["quarters"] + dimes*COINS["dimes"] + nickles*COINS["nickles"] + pennies*COINS["pennies"]
    return total

def is_transaction_successful(money_received, drink_cost):
    if money_received > drink_cost:
        #print("Sorry, there is no sufficient money")
        return True
    else:
        return False


is_on = True
profit = 0
while is_on:
    drink = input("What would you like? (espresso/latte/cappuccino)☕️:")
    if drink == "report":
        print(f'{resources["water"]}ml')
        print(f'{resources["milk"]}ml')
        print(f'{resources["coffee"]}g')
        print(f"Money: ${profit}")

    elif drink == "off":
        is_on = False

    elif is_resource_sufficient(beverage=drink):
        price = MENU[drink]["cost"]
        print(f'It will cost you $ {MENU[drink]["cost"]}')
        quarters = int(input("How many quarters?"))
        dimes = int(input("How many dimes?"))
        nickles = int(input("How many nickles?"))
        pennies = int(input("How many pennies?"))
        total = calculator()

        if is_transaction_successful(money_received=total, drink_cost=MENU[drink]["cost"]):
            rest = round((total - MENU[drink]["cost"]), 2)
            print(f"You inserted ${total}")
            print(f'Your rest is ${rest}')
            print(f"Enjoy your {drink}")
            profit += price

        else:
            print("There is no sufficient money")

