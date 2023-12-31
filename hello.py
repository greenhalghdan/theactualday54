from flask import Flask

app = Flask(__name__)
print(__name__)
@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
@app.route("/username/hello/<name>/<int:number>")
def greet(name,number):
    return f"hello {name}, you are {number} years old"

def make_bold(function):
    def wraper():
        return "<b>" + function() + "</b>"
    return wraper
def make_em(function):
    def wrapper():
        return "<em>" + function() + "</em>"
    return wrapper
def make_underline(function):
    def wrapper():
        return "<u>" + function() + "</u>"
    return wrapper

@app.route("/bye")
@make_bold
@make_em
@make_underline
def say_bye():
    return "<p>good bye!</p>"

# means we dont have to run  flask run from the termial
if __name__ == "__main__":
    app.run(debug=True)

#
# ## ********Day 54 Start**********
# ## Functions can have inputs/functionality/output
# def add(n1, n2):
#     return n1 + n2
#
# def subtract(n1, n2):
#     return n1 - n2
#
# def multiply(n1, n2):
#     return n1 * n2
#
# def divide(n1, n2):
#     return n1 / n2
#
# ##Functions are first-class objects, can be passed around as arguments e.g. int/string/float etc.
#
# def calculate(calc_function, n1, n2):
#     return calc_function(n1, n2)
#
# result = calculate(add, 2, 3)
# print(result)
#
# ##Functions can be nested in other functions
#
# def outer_function():
#     print("I'm outer")
#
#     def nested_function():
#         print("I'm inner")
#
#     nested_function()
#
# outer_function()

# ## Functions can be returned from other functions
# def outer_function():
#     print("I'm outer")
#
#     def nested_function():
#         print("I'm inner")
#
#     return nested_function
#
# inner_function = outer_function()
# inner_function
#
#
# ## Simple Python Decorator Functions
# import time
#
# def delay_decorator(function):
#     def wrapper_function():
#         time.sleep(2)
#         #Do something before
#         function()
#         function()
#         #Do something after
#     return wrapper_function
#
# @delay_decorator
# def say_hello():
#     print("Hello")
#
# #With the @ syntactic sugar
# @delay_decorator
# def say_bye():
#     print("Bye")
#
# #Without the @ syntactic sugar
# def say_greeting():
#     print("How are you?")
# decorated_function = delay_decorator(say_greeting)
# decorated_function()
#
# # end of lesson task:
# import time
# current_time = time.time()
# # print(current_time)
#
# def speed_calc_decorator(function):
#     def wrapper_function():
#         start = time.time()
#         function()
#         end = time.time()
#         print(f"{function.__name__} run time: {end-start}")
#     return wrapper_function
#
# def delay_decorator(function):
#     def wrapper_function():
#         start = time.time()
#         function()
#         end = time.time()
#         print(f"{function.__name__} run time: {end-start}")
#     return wrapper_function
#
# @speed_calc_decorator
# def fast_function():
#     for i in range(10000000):
#         i * i
#
# @speed_calc_decorator
# def slow_function():
#     for i in range(100000000):
#         i * i
#
#
# fast_function()
# slow_function()
