from currency_converter import CurrencyConverter
import tkinter as tki

c = CurrencyConverter()

def clicked():
    try:
        amount = float(entry1.get())
        curr1 = entry2.get().upper()  
        curr2 = entry3.get().upper() 
        data = c.convert(amount, curr1, curr2)
        label4.config(text=f"{amount} {curr1} = {data:.2f} {curr2}")
    except ValueError as e:
        label4.config(text=f"Error: {str(e)}")

window = tki.Tk()
window.geometry("500x360")
window.title("Currency Converter")

label = tki.Label(window, text="Currency Converter", font="Times 22 bold")
label.place(x=130, y=40)

label1 = tki.Label(window, text="Enter Amount : ", font="Times 18 bold")
label1.place(x=80, y=100)
entry1 = tki.Entry(window)
entry1.place(x=270, y=110)

label2 = tki.Label(window, text="From Currency: ", font="Times 18 bold")
label2.place(x=80, y=150)
entry2 = tki.Entry(window)
entry2.place(x=270, y=160)

label3 = tki.Label(window, text="To Currency  : ", font="Times 18 bold")
label3.place(x=80, y=200)
entry3 = tki.Entry(window)
entry3.place(x=270, y=210)

button = tki.Button(window, text="Convert", font="Times 18 bold", command=clicked)
button.place(x=290, y=250)

label4 = tki.Label(window, text="", font="Times 18 bold")
label4.place(x=180, y=300)

window.mainloop()
