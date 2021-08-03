# Module 2: Exception Handling

## Session 1: Catching Exceptions in Python

### 1.1 Normal Catching
- In Python, exceptions can be handled using a `try` statement.
- The `critical operation` which `can raise an exception` is placed inside the `try` clause. 
The code that `handles the exceptions` is written in the `except` clause.
- We can use `try ... else ...` to run a certain block of code if the code block inside try ran without any errors.
- We can also use `try ... finally ...` to execute a certain block of  code no matter what.
This case is generally used to release external resources.
(`try` with file open operation, `finally` close the file open stream)
```python
from fractions import Fraction

my_list = ['a', 0, 1, 2]

for item in my_list:
    try:
        # Calculate reciprocal value
        print('The item is', item)
        r = Fraction(1 / int(item))
    except Exception as e:
        # Print Exception class & Exception message
        print("Oops!", e.__class__, "occurred.")
        print("Error message:", e)
        print("Next entry.")
    else:
        # Print reciprocal number if the calculation has no error.
        print('Reciprocal is', r)
    finally:
        # Print notification message
        print('Reciprocal calculation is finished!')
        print()
```
```python
try:
   f = open("test.txt", encoding = 'utf-8')
   # perform file operations
finally:
   f.close()
```
### 1.2 Specific Exception Catching
- We can specify which exceptions an `except` clause should catch.
- A `try` clause can have any number of except clauses to handle different exceptions, however, 
only one will be executed in case an exception occurs.
- We can `use a tuple` of values to `specify multiple exceptions` in an `except` clause.
```python
try:
   # do something
   pass

except ValueError:
   # handle ValueError exception
   pass

except (TypeError, ZeroDivisionError):
   # handle multiple exceptions
   # TypeError and ZeroDivisionError
   pass

except:
   # handle all other exceptions
   pass
```
### 1.3 Raising Exceptions in Python
- In Python, exceptions are raised when errors occur at runtime.
We can also manually raise exceptions using the `raise` keyword.

- We can optionally pass values to the exception to clarify why that exception was raised.
```python
from fractions import Fraction

my_list = ['a', 0, 1, 2]

for item in my_list:
    try:
        # Calculate reciprocal value
        print('The item is', item)
        if not isinstance(item, int) or item <= 0:
            raise ValueError("That is not a positive number!")
        else:
            print('Reciprocal is', Fraction(1 / int(item)))
    except ValueError as ve:
        print(ve)
    finally:
        print()
```
### 1.4 Built-in Exception
There are plenty of built-in exceptions in Python that are raised when corresponding errors occur.
We can view all the built-in exceptions using the built-in `local()` function as follows:
```python
print(dir(locals()['__builtins__']))
```
Some of the common built-in exceptions in Python:

| Exception | Cause of Error |
| :---: | :--- |
| `AssertionError` | Raised when an assert statement fails. |
| `AttributeError` | Raised when attribute assignment or reference fails. |
| `EOFError` | Raised when the input() function hits end-of-file condition. |
| `FloatingPointError` | Raised when a floating point operation fails. |
| `GeneratorExit` | Raise when a generator's close() method is called. |
| `ImportError` | Raised when the imported module is not found. |
| `IndexError` | Raised when the index of a sequence is out of range. |
| `KeyError` | Raised when a key is not found in a dictionary. |
| `KeyboardInterrupt` | Raised when the user hits the interrupt key (Ctrl+C or Delete). |
| `MemoryError` | Raised when an operation runs out of memory. |
| `NameError` | Raised when a variable is not found in local or global scope. |
| `NotImplementedError` | Raised by abstract methods. |
| `OSError` | Raised when system operation causes system related error. |
| `OverflowError` | Raised when the result of an arithmetic operation is too large to be represented. |
| `ReferenceError` | Raised when a weak reference proxy is used to access a garbage collected referent. |
| `RuntimeError` | Raised when an error does not fall under any other category. |
| `StopIteration` | Raised by next() function to indicate that there is no further item to be returned by iterator. |
| `SyntaxError` | Raised by parser when syntax error is encountered. |
| `IndentationError` | Raised when there is incorrect indentation. |
| `TabError` | Raised when indentation consists of inconsistent tabs and spaces. |
| `SystemError` | Raised when interpreter detects internal error. |
| `SystemExit` | Raised by sys.exit() function. |
| `TypeError` | Raised when a function or operation is applied to an object of incorrect type. |
| `UnboundLocalError` | Raised when a reference is made to a local variable in a function or method, but no value has been bound to that variable. |
| `UnicodeError` | Raised when a Unicode-related encoding or decoding error occurs. |
| `UnicodeEncodeError` | Raised when a Unicode-related error occurs during encoding. |
| `UnicodeDecodeError` | Raised when a Unicode-related error occurs during decoding. |
| `UnicodeTranslateError` | Raised when a Unicode-related error occurs during translating. |
| `ValueError` | Raised when a function gets an argument of correct type but improper value. |
| `ZeroDivisionError` | Raised when the second operand of division or modulo operation is zero. |
## Session 2: User Defined Exception
Sometimes you may need to create your own custom exceptions that serve your purpose.
```python
class AgeNotInRangeError(Exception):
    """Exception raised for errors in the input age.

    Attributes:
        age -- input age which caused the error
        message -- explanation of the error
    """
    def __init__(self, age, message="Age is  NOT in (18, 30) range"):
        self.age = age
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f'{self.age} -> {self.message}'


age_input = int(input("Enter your age:"))
if not 18 <= age_input <= 30:
    raise AgeNotInRangeError(age_input)

```
- We have overridden the constructor of the `Exception` class to accept our own custom arguments `age` and `message`.
Then, the constructor of the parent `Exception` class is called manually with the `self.message` argument using 
`super()`.

- We customized `__str__` method of the `Exception` class is then used to display the corresponding message when 
`AgeNotInRangeError` is raised.
