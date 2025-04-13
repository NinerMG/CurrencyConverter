from tkinter import *
from tkinter import messagebox
import pyperclip

currencies = ["USD", "EUR", "PLN", "GBP", "JPY"]

def currency_converter():
    user_amount = money_texbox.get()
    currency = selected_currency.get()
    change = change_currency.get()

    print(f"amount: {user_amount} {currency} will be changed to {change}")

# creating window
window = Tk()
window.title("Currency Converter")
window.config(padx=20, pady=50)

canvas = Canvas(width=200, height=200)
canvas.grid(column=0, row=0, columnspan=3)

# adding logo image in center
logo_image = PhotoImage(file="gui_version/logo.png")
logo_image = logo_image.subsample(3,3)
canvas.create_image(100,100, image=logo_image)
canvas.grid(column=1,row=0)

# adding label and textbox to write amount of money
money_label = Label(text="Amount:")
money_label.grid(column=1, row=1)

money_texbox = Entry(width=5)
money_texbox.focus()
money_texbox.grid(column=2,row=1)

# adding currency dropbox
selected_currency = StringVar()
selected_currency.set(currencies[0])

user_currency = OptionMenu(window, selected_currency, *currencies)
user_currency.grid(column=3, row=1)

# adding information label about currency to change
change_currency_label = Label(text="Convert to")
change_currency_label.grid(column=1,row=2,columnspan=2)

# adding change currency dropbox
change_currency = StringVar()
change_currency.set(currencies[1])

currency_change = OptionMenu(window, change_currency, *currencies)
currency_change.grid(column=3, row=2)

# adding button to calculate
convert_button = Button(text="Convert", command=currency_converter)
convert_button.grid(column=2, row=3)

#result label and textbox
result_label = Label(text="Result:")
result_label.grid(column=1, row=4)
result_box = Entry(width=5)
result_box.grid(column=2, row=4)

window.mainloop()