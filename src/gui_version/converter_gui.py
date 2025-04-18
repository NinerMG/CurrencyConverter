from tkinter import *
from tkinter import messagebox

import requests
from tkinter import ttk

currencies = []

def import_currencies_names():
    global currencies
    response = requests.get("http://www.floatrates.com/daily/all.json")
    data = response.json()
    currencies = sorted([code.upper() for code in data.keys()])

def currency_converter():
    amount_to_change = money_texbox.get()
    currency_user = currency_combobox.get().lower()
    change_currency = change_currency_combobox.get().lower()

    if len(amount_to_change) == 0 or len(change_currency) == 0 or len(currency_user) == 0:
        messagebox.showinfo(title="Oooops", message="Please make sure you haven't left any fields empty.")
    else:
        try:
            amount_to_change = float(amount_to_change)
        except ValueError:
            messagebox.showerror(title="Error", message="Please enter a valid number for the amount.")
        else:
            response = requests.get(f"http://www.floatrates.com/daily/{currency_user}.json")
            data = response.json()
            rate = data[change_currency]["rate"]
            calculating_amount = amount_to_change * rate
            after_change = round(calculating_amount, 2)

            result_box.config(state="normal")
            result_box.delete(0, END)
            result_box.insert(0, f"{after_change} {(change_currency).upper()}")
            result_box.config(state="readonly")

import_currencies_names()

# =====================
#   GUI START
# =====================

# creating window

window = Tk()
window.title("Currency Converter")
window.config(padx=20, pady=50)

canvas = Canvas(window, width=150, height=150, highlightthickness=0)
logo_image = PhotoImage(file="logo.png").subsample(4, 4)
canvas.create_image(75, 75, image=logo_image)
canvas.grid(row=0, column=0, columnspan=3, pady=10)

# Amount input
money_label = ttk.Label(window, text="Amount:")
money_label.grid(column=0, row=1,padx=5, pady=5)

money_texbox = ttk.Entry(window, width=20)
money_texbox.focus()
money_texbox.grid(column=1, row=1, columnspan=2, padx=5, pady=5)

# From currency
from_label = ttk.Label(window, text="From:")
from_label.grid(column=0, row=2, padx=5, pady=5)

selected_currency = StringVar()
currency_combobox = ttk.Combobox(window, textvariable=selected_currency, values=currencies, width=17, state="readonly")
currency_combobox.set(currencies[0])
currency_combobox.grid(column=1, row=2, columnspan=2, padx=5, pady=5)

# To currency
to_label = ttk.Label(window, text="To:")
to_label.grid(column=0, row=3, padx=5, pady=5)

change_currency = StringVar()
change_currency_combobox = ttk.Combobox(window, textvariable=change_currency, values=currencies, width=17, state="readonly")
change_currency_combobox.set(currencies[1])
change_currency_combobox.grid(column=1, row=3, columnspan=2,padx=5, pady=5)

# Convert button
convert_button = ttk.Button(window, text="Convert", command=currency_converter)
convert_button.grid(column=0, row=4, columnspan=3, pady=10)

# Result
result_label = ttk.Label(window, text="Result:")
result_label.grid(column=0, row=5, padx=5, pady=5)

result_box = ttk.Entry(window, width=20, state="readonly")
result_box.grid(column=1, row=5, columnspan=2, padx=5, pady=5)


window.mainloop()