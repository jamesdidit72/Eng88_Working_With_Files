# Working with files
## Error and Exception Handling
### `try`, `except` and `finally` blocks of code
- works similar to `if` and `else:` code

### Potential Errors
```python
def greeting():  #| throws indention error, missing 'pass'
name = 'DevSecOps'
year = 2021
print(name + year)  #| throws TypeError, cannot put a string and int together

file = open('order.txt')  #| throws FileNotFoundError, file doesnt exist

try:
    file = open('order.txt')
except FileNotFoundError:
     print('File not found')
try:
    file = open('order.txt')
except FileNotFoundError as errmsg:
    # creating aliases
    print('File not found' + str(errmsg))  #|Displays a print with the error message
```

### Handling files - Reading files



- We have already opened a file, and we have begun to handle some errors that can come from it but there are many more options to be applied to the opening of a file. The key part is adding a mode to the file opening



`open(file, mode)`



| Mode |Description|
| :----: |:---- |
|'r' |This is the default mode. It Opens file for reading. |
|'w' |This Mode Opens file for writing. If file does not exist, it creates a new file. If file exists it truncates the file.|
|'x' |Creates a new file. If file already exists, the operation fails.|
|'a' |Open file in append mode. If file does not exist, it creates a new file.|
|'t' |This is the default mode. It opens in text mode.|
|'b' |This opens in binary mode.
|'+' |This will open a file for reading and writing (updating)|

## Task 1
### Writing to a file
```python
# create a function to called open_with_to_write_to_file write/add/append
# display the data with the added data - item names - pizza, cake, avacado, biryani, pasta

def open_with_to_write_to_file(file):
    try:
        with open('order.txt', 'a') as file:  # 'a' = append
            file.write('\nPizza\nCake\nAvocado\nBiryani\nPasta')
    except FileNotFoundError as errmsg:
        print('Sorry, file not found: ' + str(errmsg))
    finally:
        return 'Thank you for visiting'  # return removes the 'none' message

open_with_to_write_to_file('order.txt')
```
#### Uses 'a' from the table for adding to the file
### Iteration 2
- added list
```python
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

```