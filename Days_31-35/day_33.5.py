# Warm Up - Day 33 of 100 Days of Code Challenge
# Kanye Quote Generator
import tkinter as tk
import requests


def generate_quote():
    response = requests.get(url="http://api.kanye.rest")
    response.raise_for_status()
    kanye_quote = response.json()['quote']
    canvas.itemconfig(quote_text, text=kanye_quote)


root = tk.Tk()
root.config(pady=40, padx=40)
root.title("Kanye says...")

canvas = tk.Canvas(width=300, height=414)
background = tk.PhotoImage(file='background.png')
canvas.create_image(150, 207, image=background)
quote_text = canvas.create_text(150, 195, width=270, justify='center', font=('Ariel', 15, 'bold'),
                                text="", fill="white")
canvas.pack()

kanye_head = tk.PhotoImage(file='kanye.png')
kanye_button = tk.Button(image=kanye_head, command=generate_quote)
kanye_button.pack()

generate_quote()

root.mainloop()
