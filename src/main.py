amount_of_currency = 0
amount_in_dollars = 0
exchange_rate = 1
currency_name = ""

def currency():
    name = input("Enter your currency\n")
    global currency_name
    currency_name = f"{name}coin"

def amount_possessed():
    global amount_of_currency
    amount_of_currency = int(input(f"Please, enter the number of {currency_name} you have:\n"))
    # print(f"I have {amount} {currency_name}.")
    return amount_of_currency

def currency_to_dollars():
    global amount_in_dollars, exchange_rate
    exchange_rate = float(input("Please, enter the exchange rate:\n"))
    amount_in_dollars = amount_of_currency * exchange_rate

    if amount_in_dollars.is_integer() and exchange_rate.is_integer():
        amount_in_dollars = int(amount_in_dollars)

    print(f"{amount_of_currency} {currency_name} cost {amount_in_dollars} dollars.")
    return amount_in_dollars

def rich_or_not():
    if amount_in_dollars > 1000:
        print("I am rich! Yippee!")
    else:
        print("Ohh I need to earn much more")

if __name__ == "__main__":
    currency()
    amount_possessed()
    currency_to_dollars()
    # rich_or_not()

