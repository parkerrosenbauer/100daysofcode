# Day 54 of 100 Days of Code Challenge
# Intro to Flask, command line, decorator functions

from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'


if __name__ == "__main__":
    app.run()


# Practice with function decorators
# import time

# def speed_calc_decorator(function):
#     def timer():
#         start = time.time()
#         function()
#         end = time.time()
#         total = end - start
#         print(f"{function.__name__} run speed = {total}s")
#
#     return timer
#
# 
# @speed_calc_decorator
# def fast_function():
#     for i in range(10000000):
#         i * i
#
#
# @speed_calc_decorator
# def slow_function():
#     for i in range(100000000):
#         i * i
#
#
# fast_function()
# slow_function()
