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