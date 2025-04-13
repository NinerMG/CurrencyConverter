import json
from json import JSONDecodeError
import requests

data_link = ""

def get_amount():
    amount = float(input("Enter amount you want to exchange\n"))
    return amount

def get_user_currency():
    user_currency = input("Enter currency you have:\n").lower()
    return user_currency

def get_exchange_currency():
    exchange_code = input("Enter currency code you want to exchange:\n").lower()
    return exchange_code

def get_url(short):
    return f"http://www.floatrates.com/daily/{short}.json"

def get_data(url_link):
    try:
        response = requests.get(url_link)
        data = response.json()
    except requests.RequestException:
        print("Error! Problems with url.")
    except JSONDecodeError:
        print("Error! Problems with json file.")
    else:
        return data

def save_to_json(url_link):
    data = get_data(url_link)

    combined_data = {
        "eur": data.get("eur"),
        "usd": data.get("usd")
    }
    with open("data.json", "w") as file:
        json.dump(combined_data, file, indent=2)

def read_from_json(currency):
    with open("data.json", "r") as file:
        data = json.load(file)
        return data[currency]["rate"]

def calculate_exchange_amount(amount, rate):
    amount_after = amount * rate
    result = round(amount_after, 2)
    return result

def checking_cache(exchange_currency):
    print("Checking the cache...")

    if exchange_currency == "usd" or exchange_currency == "eur":
        print("Oh! It is in the cache!")
        return read_from_json(exchange_currency)
    else:
        print("Sorry, but it is not in the cache!")
        return get_data(data_link)[exchange_currency]["rate"]

def currency_converter():
    #get data from user
    user_currency = get_user_currency()
    while True:
        exchange_currency = get_exchange_currency()
        amount_to_exchange = get_amount()

        # create link to data
        global data_link
        data_link = get_url(user_currency)

        # save eur and usd to json file
        save_to_json(data_link)

        # get rate from json file or again from url
        rate = checking_cache(exchange_currency)

        # calculate amount from exchange
        amount_after_exchange = calculate_exchange_amount(amount_to_exchange, rate)
        print(f"You received {amount_after_exchange} {exchange_currency.upper()}.")

        # repeat exchange to another currency
        again = input("\nDo you want to make another exchange? (yes/no): ").strip().lower()
        if again not in ["yes", "y"]:
            print("Goodbye!")
            break
if __name__ == "__main__":
    currency_converter()
