import json
import requests

def get_url():
    currency_code = input("Enter currency code: ").lower()
    return  f"http://www.floatrates.com/daily/{currency_code}.json"

def get_request(url_link):
    try:
        response = requests.get(url_link)
        data = response.json()
    except requests.RequestException:
        print("Error with request")
    except json.JSONDecodeError:
       print("Error with reading JSON")


    with open("data.json", "w") as file:
        json.dump(data, file, indent=2)

def print_data(currency):
    try:
        with open("data.json", "r") as file:
            data = json.load(file)
            if currency in data:
                print(data[currency])
            else:
                print(f"{currency} not found in the data.")
    except FileNotFoundError:
        print("Data file not found")

if __name__ == "__main__":
    url_link = get_url()
    get_request(url_link)
    print_data("eur")
    print_data("usd")