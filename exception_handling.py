# `try`, `except` and `finally` blocks of code

# def greeting():  #| throws indention error, missing 'pass'


# name = 'DevSecOps'
# year = 2021
# print(name + year)  #| throws TypeError, cannot put a string and int together

# file = open('order.txt')  #| throws FileNotFoundError, file doesnt exist

# try:
#     file = open('order.txt')
# except FileNotFoundError:
#     print('File not found')

# try:
#     file = open('order.txt')
# except FileNotFoundError as errmsg:
#     # creating aliases
#     print('File not found' + str(errmsg))  #|Displays a print with the error message


try:
    file = open('order.txt')
except FileNotFoundError as errmsg:
    # creating aliases
    print('File not found' + str(errmsg))
finally:
    print('Thank you for visiting')
