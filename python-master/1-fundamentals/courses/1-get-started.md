# Module 1: Get Started

## Session 1: Python Input, Output and Import 
In this session, we will go through built-in functions `input()` and `print()` to perform I/O task in Python.
Then, we will learn how to `import` modules and use them in our scripts

### 1.1 Python Input
In python, we can use `input()` method to retrieve the input from user. The syntax for this method is `input([prompt])`
where `prompt` is the string we want to display on the screen and it is optional
```python
my_name = input('Enter your name: ')
# System will show => Enter your name:
# User then input `rocky`
print(my_name)
# Output => rocky
``` 

### 1.2 Python Output
In this training package, we will use `print()` to output data to standard output device: `screen/console`.
We can output data into a file, but we will work with it later.

Let go through several examples:
```python
# Example 1
print('Welcome to Python.')    # Output => 'Welcome to Python.'
# Example 2
member = 'Rocky'
print('Good morning,', member) # Output => 'Good morning, Rocky
``` 
We can notice in `Example 2` that there is a space was added between the string and the value of variable `member`. 
This is the default due to the syntax of the print, but we can change it.

The actual syntax of the `print()` function:
`
print(*objects, sep= ' ', end='\n', file=sys.stdout, flush=False)
`
* `objects` is the values will be printed.
* `sep` is the separator used between values.
* `end` is printed after all values are printed. By default, it would be into a new line.
* `file` is the object where the values are printed. By default, it would be `sys.stdout` (screen/console).

So, we can try with some practices.
```python
print('A', 'B', 'C', 'D')           # Output => A B C D
print(1, 2, 3, 4, sep='+')          # Output => 1+2+3+4
print(1, 2, 3, 4, sep='*', end='=') # Output => 1*2*3*4=
```
In some cases, we would want to format the output. This can be done using `str.format()` method.
```python
a = 1; b = 2
print('The value of a is {} and b is {}'.format(a, b))
# Output => The value of a is 1 and by is 2
```
In here, the `{}` are used as the placeholders. We can also specify the order in which the value should be printed.
```python
print('I like {0} and {1}'.format('Apple', 'Banana')) # Output => I like Apple and Banana
print('I like {1} and {0}'.format('Apple', 'Banana')) # Output => I like Banana and Apple
```
We can also use keyword to format the string:
```python
print('Hello {name}, {greeting}'.format(greeting = 'good morning', name = 'Rocky'))
# Output => Hello Rocky, good morning
```

### 1.3 Python Import
When writing a complex application, it would be a good way to break it into modules.
A module in Python is a file contains Python definitions and statements. We will learn more about module in 
[Python Module]() session.

To import a module we use the keyword `import`.
For example, we will import the `math` module and try to output the pi value:
```python
import math
print(math.pi)
```
The output would be `3.141592653589793`. By import the `math` module, all of it definition will be available in our 
scope.

We also can import some specific attributes/functions only by using `from` keyword. For example:
```python
from math import pi
print(pi)
```

While importing a module, Python will look at several places defined in `sys.path`. It is a list of directory locations.
We can also add our own location to this list. To view the path list, we can use this part of code:
```python
import sys
print(sys.path)
```

## Session 2: Python keyword & identifier
In this session, we will learn about keywords (reserved words in Python) and identifiers 
(names given to variables, functions, etc).

### 2.1 Python keyword (reserved word)
Keywords are the reserved words in Python. The keywords cannot be used as a `variable` name, `function` name or any
other identifier. They are used to define the syntax of Python script.

In python, keywords are `case sensitive`. In python 3.8, there are 35 keywords. 
All the keywords except `True`, `False` and `None` are in lowercase and they must be written as they are.

To list all of the keywords, we use this example:
```python
import keyword
print(keyword.kwlist)
``` 

||||||||
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | 
| `False` | `None` | `True` | `and` | `as` | `assert` | `async` |
| `await` | `break` | `class` | `continue` | `def` | `del` | `elif` |
| `else` | `except` | `finally` | `for` | `from` | `global` | `if` |
| `import` | `in` | `is` | `lambda` | `nonlocal` | `not` | `or` |
| `pass` | `raise` | `return` | `try` | `while` | `with` | `yield` |

### 2.2 Python identifier
An `identifier` is the name given to entities such as `class`, `function`, `variable`, etc. It helps to classify an 
entity to another.

There are some rules to define an identifier:
* It can be the combination of lowercase letters `[a-z]`, uppercase letters `[A-Z]`, digits `[0-9]` 
or an underscore `_`.
For Example: `my_variable`, `MyClass`, `plus_two_number()`.
* It cannot start with a `digit`. `1variable` is invalid, but `variable1` is valid.
* Keywords cannot be used as identifiers.
* Special symbols like `!`,`@`, `#`, `$`, `%` cannot be used as well.

**Important Notes**
* Python language is _**case sensitive**_. That means `var` and `Var` are two different identifiers.
* Using meaningful identifiers are encouraged. The `s = 10` is a valid but `sum = 10` would make more sense.
* Multiple words can be separated by `_`. For example: `a_long_name_variable`.  

## Session 3: Python Statement, Indentation, Comment, Function & Docstrings
In this session, we will learn about statements and comments in Python.

### 3.1 Python Statement
The instructions that a Python interpreter can execute are called statements:
* Assignment statement: `a = 1`.
* Condition statement: `if`.
* Loop statement: `for`, `while`.

For example:
```python
balance = 1000
if balance > 0:
    print('Your balance is', balance)
``` 
The statement can be written in multiple lines by using line continuation character `\ \`. 
Statements contained within the `[]`, `{}`, or `()` do not need to use it.
 ```python
# Multiple lines using '\'
a = 1 + 2 + 3 + \
     4 + 5 + 6 + \
     7 + 8 + 9
# Multiple lines in brackets
days = ['Monday', 'Tuesday', 'Wednesday',
        'Thursday', 'Friday']
```
We will go into details on condition and loop statements in [Module 2 - Python Flow Control](2-flow-control.md).

### 3.2 Python Indentation
Most of the programming languages like PHP, JavaScript and Java use braces `{ }` to define a block of code.
Python, however, uses indentation.

A code block (body of a function, loop, etc.) starts with indentation and ends with the first un-indented line.
The amount of indentation is up to you, but it must be consistent throughout that block.
Generally, `four whitespaces` are used for indentation and are preferred over `tabs`. For example:
```python
number = int(input('Input a number:'))
for i in range(0, number):
    if i % 2 == 0:
        print(i, 'is an even number.')
    else:
        print(i, 'is an odd number.')
```

### 3.3 Python Comment
In Python, we use the hash `#` symbol to start writing a comment. With multiple comment lines, we also use `#` as well.
```python
# Print out a sample text
print('My test output')

# This is the function description,
# it will returns the test output.
def my_function():
    return 'my function output' 
```
### 3.4 Python Function
In Python, the syntax of the function would be like this.
```python
def greet(name):
    """
    This function greets to
    the person passed in as
    a parameter
    """
    print("Hello, " + name + ". Good morning!")

# Output -> "Hello, Rocky. Good morning!" 
greet('Rocky')
```
### 3.5 Python Docstrings
By convention, the triple quotes `"""` that appear right after the function, method or class definition are docstrings 
(documentation strings).

Docstrings are associated with objects and can be accessed using the `__doc__` attribute.
```python
def greet(name):
    """
    This function greets to the person passed in as a parameter
    """
    print("Hello, " + name + ". Good morning!")

# Output -> 'This function greets to the person passed in as a parameter'
print(greet.__doc__)
```
## Session 4: Python Operator
Operators are special symbols in Python that carry out arithmetic or logical computation.
The value that the operator operates on is called the operand.
```python
>>> 2+3
5
```
For example, `+` is the operator that performs addition. `2` and `3` are the operands and `5` is the output of the 
operation.
### 4.1 Arithmetic Operators

| Operator | Meaning | Example |
| :---: | --- | --- |
| + | Add two operands | x + y + 2|
| - | Subtract right operand from the left | x - y - 2|
| * | Multiply two operand| x * y|
| / | Divide lef operand by the right one (results in float) | x * y |
| % | Modulus - remainder of the division of left operand by the right |  x % y |
| // | Floor division - division that results into whole number adjusted to the left in the number line | x // y|
| ** | Exponent - left operand raised to the power of right | x ** y |
```python
x = 11
y = 4

print('x + y =',x+y) # Output: x + y = 15

print('x - y =',x-y) # Output: x - y = 7

print('x * y =',x*y) # Output: x * y = 44

print('x / y =',x/y) # Output: x / y = 2.75

print('x // y =',x//y) # Output: x // y = 2

print('x ** y =',x**y) # Output: x ** y = 50625
```
### 4.2 Comparison Operators
Comparison operators are used to compare values.
It returns either `True` or `False` according to the condition.

| Operator | Meaning | Example |
| :---: | --- | --- |
| > | Greater than - True if left operand is greater than the right | x > y |
| < | Less than - True if left operand is less than the right | x < y |
| == | Equal to - True if both operands are equal | x == y |
| != | Not equal to - True if operands are not equal | x != y |
| >= | Greater than or equal to - True if left operand is greater than or equal to the right |  x >= y |
| <= | Less than or equal to - True if left operand is less than or equal to the right | x <= y|
```python
x = 10
y = 12

print('x > y is',x>y) # Output: x > y is False

print('x < y is',x<y) # Output: x < y is True

print('x == y is',x==y) # Output: x == y is False

print('x != y is',x!=y) # Output: x != y is True

print('x >= y is',x>=y) # Output: x >= y is False

print('x <= y is',x<=y) # Output: x <= y is True
```
### 4.3 Logical Operators
Logical operators are the `and`, `or`, `not` operators.

| Operator | Meaning | Example |
| :---: | --- | :---: |
| and | True if both the operands are true | x and y|
| or | True if either of the operands is true | x or y|
| not | True if operand is false (complements the operand) |not x|
```python
x = True
y = False

print('x and y is',x and y) # Output x and y is False

print('x or y is',x or y) # Output x and y is True

print('not x is',not x) # Output x and y is False
```
### 4.4 Bitwise Operators
Bitwise operators act on operands as if they were strings of binary digits. They operate bit by bit, hence the name.

For example, 2 is `10` in binary and 7 is `111`.

In the table below: Let `x` = 10 (`0000 1010`) and y = `4` (`0000 0100`)

| Operator | Meaning | Example |
| :---: | --- | --- |
| & | Bitwise AND | x & y = 0 (`0000 0000`)|
| &#124; | Bitwise OR | x &#124; y = 14 (`0000 1110`)|
| - | Bitwise NOT | -x = -11 (`1111 0101`)|
| ^ | Bitwise XOR | x^y = 14 (`0000 1110`)|
| &gt;&gt; | Bitwise Right Shift | x &gt;&gt; 2 = 2 (`0000 0010`)|
| << | Bitwise Left Shift | x << 2 = 40 (`0010 1000`)|
### 4.5 Assignment Operators
Assignment operators are used in Python to assign values to variables.

| Operator | Example | Equivalence |
| :---: | --- | --- |
| = | x = 2 | x = 2 |
| += | x += 2 | x = x + 2 |
| -= | x -= 2 | x = x - 2 |
| *= | x *= 2 | x = x * 2 |
| /= | x /= 2 | x = x / 2 |
| %= | x %= 2 | x = x % 2 |
| //= | x //= 2 | x = x // 2 |
| **= | x **= 2 | x = x ** 2 |
| &= | x &= 2 |  x = x & 2 |
| &#124;= | x &#124;= 2 | x  = x &#124; 2 |
| ^= | x ^= 2 | x = x ^ 2|
| &gt;&gt;= | x &gt;&gt;= 2 | x = x &gt;&gt; 2 |
| <<= | x <<= 2 | x = x << 2 |
### 4.6 Special Operators
**Identity Operators**

`is` and `is not` are the identity operators in Python. 
They are used to check if two values (or variables) are located on the same part of the memory.
Two variables that are equal does not imply that they are identical.
```python
a1 = 1
b1 = 1
a2 = 'Hello'
b2 = 'Hello'
a3 = [1, 2, 3]
b3 = [1, 2, 3]

# Output: True
# a1 and b1 reference to the same memory location that stores '1'
print(a1 is b1)

# Output: False
# a2 and b2 reference to the same memory location that stores 'Hello'
print(a2 is not b2) 

# Output: False
# a3 and b3 look the same, but they are  located separately.
print(a3 is b3) 

# Output: False
# a3[0] and a1 reference to the same memory location that stores '1'
print(a3[0] is not a1)
```

**Membership Operators**

`in` and `not in` are the membership operators in Python.
They are used to test whether a value or variable is found in a sequence 
(`string`, `list`, `tuple`, `set` and `dictionary`).
```python
x = 'Hello python'
y = {
    1: 'a',
    2: 'b'
}

# Output: True
print('H' in x)

# Output: True (Python is case sensitive)
print('hello' not in x)

# Output: True
print(1 in y)

# Output: False
print('a' in y)
```
[**Back to Module List**](../README.md)