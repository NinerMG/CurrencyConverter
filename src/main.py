amount = 0
dollars = 0
currency_name = ""

def currency():
    name = input("Enter your currency\n")
    global currency_name
    currency_name = f"{name}coin"

def amount_possessed():
    global amount
    amount = int(input("Enter your amount\n"))
    print(f"I have {amount} {currency_name}.")
    return amount

def currency_to_dollars():
    global dollars
    dollars = amount * 100
    print(f"{amount} {currency_name} cost {dollars} dollars.")
    return dollars

def rich_or_not():
    if dollars > 1000:
        print("I am rich! Yippee!")
    else:
        print("Ohh I need to earn much more")

if __name__ == "__main__":
    currency()
    amount_possessed()
    currency_to_dollars()
    rich_or_not()

