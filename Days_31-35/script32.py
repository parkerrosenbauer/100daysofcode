# Day 32 of 100 Days of Code Challenge
# Auto Emailer
import smtplib
import datetime as dt
import pandas as pd
from random import choice

LETTERS = ["letter_templates/letter_1.txt", "letter_templates/letter_2.txt", "letter_templates/letter_3.txt"]
USER = "pythonbot97@gmail.com"
PASS = "pythonpassword"
now = dt.datetime.now()


def send_letter(name):
    with open(choice(LETTERS), mode='r') as file:
        bday_letter = file.read()
        bday_letter = bday_letter.replace("[NAME]", name)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=USER, password=PASS)
        connection.sendmail(
            from_addr=USER,
            to_addrs=all_bdays.email.loc[name],
            msg=f"Subject:Happy Birthday!\n\n{bday_letter}")


all_bdays = pd.read_csv('birthdays.csv', index_col="name")
today_bdays = all_bdays[(all_bdays.month == now.month) & (all_bdays.day == now.day)]

if len(today_bdays) > 0:
    for person in today_bdays.index:
        send_letter(person)
