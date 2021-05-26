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


# try:
#     file = open('order.txt')
# except FileNotFoundError as errmsg:
#     # creating aliases
#     print('File not found' + str(errmsg))
# finally:
#     print('Thank you for visiting')
# def open_using_with_and_print(file):
#     try:
#         with open('order.txt',
#                   'r') as file:  # with is a method, open opens file, 'file_name' = file name, 'r' = reads file, as file sets the file as a variable
#             for line in file.readlines():  # reads each line in the file  # 'readline()' only reads each letter
#                 print(line.rstrip('\n'))  # splits the lines up individually
#     # try block of code ends
#     except FileNotFoundError as errmsg:
#         print('Sorry, file not found: ' + str(errmsg))
#     finally:
#         return 'Thank you for visiting'  # return removes the 'none' message


# print(open_using_with_and_print('order.txt'))


# create a function to called open_with_to_write_to_file write/add/append
# display the data with the added data - item names - pizza, cake, avacado, biryani, pasta

def open_with_to_write_to_file(file, item_list):
    try:
        with open('order.txt', 'a') as file:  # 'a' = append
            for item in item_list:
                file.write('\n' + item)
    except FileNotFoundError as errmsg:
        print('Sorry, file not found: ' + str(errmsg))
    finally:
        return 'Thank you for visiting'  # return removes the 'none' message

add_to_file = ['Pizza','Cake','Avocado','Biryani','Pasta']
open_with_to_write_to_file('order.txt', add_to_file)
