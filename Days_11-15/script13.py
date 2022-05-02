# Day 13 of 100 Days of Code Challenge
# Debugging

# Describe Problem
# def my_function():
#     for i in range(1, 20):  # the problem with this code is here, the range function stop parameter is exclusive, so i will never equal 20
#         if i == 20:
#             print("You got it")
# my_function()

# # Reproduce the Bug
# from random import randint
# dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
# # the problem with this code is below, randint is generating numbers between 1-6, but the list indices for dice_imgs are in the range 0-5
# dice_num = randint(1, 6)
# print(dice_imgs[dice_num]) #if dice_num is replaced with 6, this bug will happen everytime the code is run

# # Play Computer
# year = int(input("What's your year of birth?"))
# if year > 1980 and year < 1994:
#     print("You are a millenial.")
# elif year > 1994:
#     print("You are a Gen Z.")
# # the problem with this code block is that if someone's birth year is 1994, they won't fall into either classification of millenial or gen z.
# # to fix, either the if block needs to be changed to year > 1980 and year <= 1994, or the elif block needs to be changed to year >= 1994

# # Fix the Errors
# age = input("How old are you?")
# if age > 18:
# # the below statement is highlighted in red, needing to be indented under the if statement
# print("You can drive at age {age}.")
# # the indentation isn't the only error though. The if statement is evaluating if age > 18, but age is currently a string, so it can't be evaluated
# # the other error is that an f string is in the print statement, but there isn't an 'f' before the string starts

# Print is Your Friend
# pages = 0
# word_per_page = 0
# pages = int(input("Number of pages: "))
# word_per_page == int(input("Number of words per page: "))
# total_words = pages * word_per_page
# print(total_words)
# # when evaluating this code block, no matter what was inputed into pages and word_per_page, the total_words = 0.
# # to easily find the bug, both pages and word_per_page could be printed after inputting values, to see what was going wrong.
# # when word_per_page always evaluated to 0, it was easier to spot that word_per_page wasn't being reassigned to the new input
# # because there were two equals signs (==) evaluating it to the input rather than a single one reassigning it.

# Use a Debugger
# def mutate(a_list):
#     """multiply values in a list by 2"""
#     b_list = []
#     for item in a_list:
#         new_item = item * 2
#     b_list.append(new_item)
#     print(b_list)
# mutate([1, 2, 3, 5, 8, 13])
# # using pythontutor.com showed each item in the list being updated, but then overrode by the next item before it could be added
# # into the list. To make this code work, b_list.append(new_item) needs to be in the for loop.
