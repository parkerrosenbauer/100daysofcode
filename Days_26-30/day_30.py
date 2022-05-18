# Day 30 of 100 Days of Code
# Improved Password Manager
from tkinter import *
import json
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_pass():
    password_name.delete(0, END)

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    pass_list = [choice(letters) for _ in range(randint(8, 10))]
    pass_list += [choice(symbols) for _ in range(randint(2, 4))]
    pass_list += [choice(numbers) for _ in range(randint(2, 4))]

    shuffle(pass_list)

    pass_word = ''.join(pass_list)

    password_name.insert(0, pass_word)
    pyperclip.copy(pass_word)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def write_data(to_write):
    with open(file='passwords.json', mode='w') as file:
        json.dump(to_write, file, indent=4)


def save_password():
    """Take website, email, and password input and save to file"""
    website = website_name.get()
    user = user_name.get()
    password = password_name.get()

    info = {
        website: {
            "username": user,
            "password": password
        }
    }

    # Confirm info is completely filled in
    if website == "" or user == "":
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
    else:
        # Confirm inputs
        is_ok = messagebox.askokcancel(title=website, message=f"Confirm the details entered: \n\nUsername: {user}\n"
                                                              f"Password: {password}\n\nOK to save?")
        if is_ok:
            try:
                with open(file='passwords.json', mode='r') as file:
                    data = json.load(file)
            except FileNotFoundError:
                write_data(info)
            else:
                data.update(info)
                write_data(data)
            finally:
                website_name.delete(0, END)
                password_name.delete(0, END)
                add_password.config(text="Add")


# ---------------------------- SEARCH WEBSITES ------------------------------- #


def find_site():
    try:
        with open(file='passwords.json', mode='r') as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(title="Oops", message="You must save a username and password to a website first.")
    else:
        website = website_name.get()
        if website in data:
            username = data[website]["username"]
            password = data[website]["password"]
            update = messagebox.askyesno(title=website, message=f"Username: {username}\nPassword: {password}\n\n"
                                                                f"Would you like to update the password?")
            if update:
                add_password.config(text="Update")
        else:
            messagebox.showinfo(title="Oops", message=f"There is no saved password for {website}.")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.config(padx=50, pady=50)
window.title("Password Manager")

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file='logo.png')
canvas.create_image(120, 100, image=logo_img)
canvas.grid(row=0, column=1)

# Labels
website_prompt = Label(text="Website:")
website_prompt.grid(row=1, column=0, pady=5)
user_prompt = Label(text="Email/Username:")
user_prompt.grid(row=2, column=0)
password_prompt = Label(text="Password:")
password_prompt.grid(row=3, column=0, pady=5)

# Entry boxes
website_name = Entry(width=24, font=12)
website_name.grid(row=1, column=1)
website_name.focus()
user_name = Entry(width=37, font=12)
user_name.insert(0, "parkerrosenbauer@gmail.com")
user_name.grid(row=2, column=1, columnspan=2)
password_name = Entry(width=24, font=12)
password_name.grid(row=3, column=1)

# Buttons
search_website = Button(text="Search", width=14, command=find_site)
search_website.grid(row=1, column=2)
gen_password = Button(text="Generate Password", command=generate_pass)
gen_password.grid(row=3, column=2)
add_password = Button(text="Add", width=47, command=save_password)
add_password.grid(row=4, column=1, columnspan=2)

window.mainloop()
