amount = 0
currency_name = "conicoins"

currency_exchange = {
    "RUB":{
      "name": "Russian Ruble",
        "short_name": "RUB",
        "exchange": 2.98
    },
    "ARS": {
        "name": "Argentine Peso",
        "short_name": "ARS",
        "exchange": 0.82
    },
    "HNL": {
        "name": "Honduran Lempira",
        "short_name": "HNL",
        "exchange": 0.17
    },
    "AUD": {
        "name": "Australian Dollar",
        "short_name": "AUD",
        "exchange": 1.9622
    },
    "MAD": {
        "name": "Moroccan Dirham",
        "short_name": "MAD",
        "exchange": 0.208
    },
}

def get_amount():
    global amount
    amount = float(input(f"Please, enter the number of {currency_name} you have\n"))

def calculate_currency():
    for main_key, inner_key in currency_exchange.items():
        calculated_amount = amount * inner_key["exchange"]
        calculated_amount = round(calculated_amount,2)
        amount_round = round(amount,2)
        print(f"I will get {calculated_amount} {inner_key['short_name']} from the sale of {amount_round} {currency_name}.")

if __name__ == "__main__":
    get_amount()
    calculate_currency()