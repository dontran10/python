# Module 2: Flow Control
## Session 1: Condition Statements
### 1.1 if ... else statement
Condition statements are used for decision making when we want to execute a piece of code when a certain condition is 
satisfied.

In Python we use the `if ... elif ... else` for this purpose. (_**In Python, we do not have `switch ... case ...` statement.**_)
```python
number = 4
if number > 0:
    print(number, 'is a positive number.')
print('This line is always printed.')
``` 
```python
number = -1
if number > 0:
    print(number, 'is a positive number.')
else:
    print(number, 'is NOT a positive number.')
print('This line is always printed.')
```
```python
number = 0
if number > 0:
    print(number, 'is a positive number.')
elif number < 0:
    print(number, 'is a negative number.')
else:
    print(number 'is a zero number.')
print('This line is always printed.')
```
### 1.2 Nested if ... else statement
We use indentation to figure out the level of nesting in Nested condition statements.
```python
number = 10
if number >= 0:
    if number == 0:
        print('ZERO number')
    else:
        print('POSITIVE number')
else:
    print('NEGATIVE number')
```
## Session 2: Loop Statements
### 2.1 for Statement
In Python, we use `for` statement to traverse a sequence (list, tuple, string) or other iterable objects.
```python
numbers = [1, 2, 3, 4, 5]
s = 0
for val in numbers:
   s += val
print('The sum is', s)
```
**The range() function**

This is a very common function to help us generate a sequence of numbers.
For example, `range(10)` will generate numbers from 0 to 9 (10 numbers).

We can define the start, stop, and step size as `range(start, stop, step_size)`.
For example, `range(1, 10, 2) -> (1, 3, 5, 7, 9)`.

The `range` object is "**lazy**", It does not store all values in memory. It only remembers the start, stop, step size
and generate the next number on the go. It is `NOT an ITERATORS`, it supports `in`, `len`, and `__getitem__` operations.
```python
# Output -> range(10)
print(range(10))
```
```python
# Output -> (1, 3, 5, 7, 9)
print(list(range(1, 10, 2)))
```
```python
# Output -> total = 45 (sum all numbers in [1, 2, 3, 4, 5, 6, 7, 8, 9])
total = 0
for i in range(1, 10, 1):
    total += i
print(total)
```
### 2.2 while Statement
The `while` loop in Python is used to iterate over a block of code as long as the test condition is true.
```python
n = 10
s = 0
i = 1

while i <= n:
    s += i
    i += 1

# print the sum
print("The sum is", s)
```
### 2.3 break & continue
The `break` statement terminates the loop containing it.
Control of the program flows to the statement immediately after the body of the loop.
```python
for val in "python":
    if val == "t":
        break
    print(val)

print("The end")
# Output
# p
# y
# The end
```
The `continue` statement is used to skip the rest of the code inside a loop for the current iteration.
```python
for val in "python":
    if val == "t":
        continue
    print(val)

print("The end")
# Output
# p
# y
# h
# o
# n
# The end
```
### 2.4 pass statement
In Python, the `pass` statement is a null statement.

The difference between a `comment` and a `pass` statement is that while the interpreter ignores a `comment` entirely, 
`pass` is not ignored.

Nothing happens when the `pass` is executed. It results in `no operation (NOP)`.
We generally use it as a `placeholder`.
```python
def function(args):
    pass

class SampleClass:
    pass
```
[**Back to Module List**](../README.md)