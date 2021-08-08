import tkinter as tk
from tkinter import *
import tkinter.messagebox
root = tk.Tk()
root.title("CurrencyConvertorPy")
Tops = Frame(root, bg='#e6e5e5', pady=2, width=1850, height=100, relief="ridge")
Tops.grid(row=0, column=0)
headlabel = tk.Label(Tops, font=('lato black', 19, 'bold'), text='CurrencyConverterPy'bg='#e6e5e5', fg='black')
headlabel.grid(row=1, column=0, sticky=W)

currency1 = tk.StringVar(root)
currency2 = tk.StringVar(root)
currency1.set("currency")
currency2.set("currency")
def RealTimeCurrencyConversion():
    from forex_python.converter import CurrencyRates
    c = CurrencyRates()
    from_currency = currency1.get()
    to_currency = currency2.get()
    if (Amount1_field.get() == ""):
        tkinter.messagebox.showinfo("Error !!", "Amount Not Entered.\n Please a valid amount.")
    elif (from_currency == "currency" or to_currency == "currency"):
        tkinter.messagebox.showinfo("Error !!",
                                    "Currency Not Selected.\n Please select FROM and TO Currency form menu.")
    else:
        new_amt = c.convert(from_currency, to_currency, float(Amount1_field.get()))
        new_amount = float("{:.4f}".format(new_amt))
        Amount2_field.insert(0, str(new_amount))
def clear_all():
    Amount1_field.delete(0, tk.END)
    Amount2_field.delete(0, tk.END)
