# Day 27 of 100 Days of Code Challenge
# GUI Unit Converter
import tkinter as tk


def m_to_km():
    mile_value = int(mile_input.get())
    km_result = round(mile_value * 1.609, 1)
    result["text"] = str(km_result)


window = tk.Tk()
window.title("Miles to Km")
window.minsize(width=240, height=50)
window.config(padx=20, pady=20)

# labels
miles = tk.Label(text="Miles")
miles.config(padx=5)
miles.grid(column=2, row=0)

equal_to = tk.Label(text="is equal to")
equal_to.grid(column=0, row=1)

result = tk.Label(text="0")
result.grid(column=1, row=1)

km = tk.Label(text="Km")
km.grid(column=2, row=1)

# button
button = tk.Button(text="Calculate", command=m_to_km)
button.grid(column=1, row=2)

# entry
mile_input = tk.Entry(width=10)
mile_input.grid(column=1, row=0)

window.mainloop()
