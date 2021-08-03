# Module 1: Function, Class and Object (OOP Concepts)

## Session 1: Function
In Python, a function is a group of related statements that performs a specific task.

Functions help break our program into smaller and modular chunks.
As our program grows larger and larger, functions make it more organized and manageable.

### 1.1 Syntax of Function
- Keyword `def` that marks the start of the function header.
- A function name to uniquely identify the function.
Function naming follows the same rules of writing [`identifiers`](../../1-fundamentals/courses/1-get-started.md) in Python.
- Parameters (arguments) through which we pass values to a function. They are optional.
- A colon (`:`) to mark the end of the function header.
- Optional documentation string (`docstring`) to describe what the function does.
- One or more valid python statements that make up the function body.
Statements must have the same indentation level (usually 4 spaces).
` An optional `return` statement to return a value from the function.

To call a function we simply type the `function name` with appropriate `parameters`.

**Syntax**
```python
def function_name(parameters):
    """docstring"""
    statement(s)
```
**Examples**
```python
def say_hello(name):
    """This function generate welcome string to the person name passed in."""
    print('Hello, ', + name + '. Good Morning!')

say_hello('Rocky')
```
```python
def check_possitive_number(number):
    """This function will check the number passed in is a positive number or not."""
    if number > 0:
        return True
    return False
```
### 1.2 Function argument
**Default Arguments**
```python
def hello(name, msg="Good morning!"):
    """
    This function say hello to the person with the provided message.
    
    If the message is not provided,it defaults to "Good morning!"
    """

    print("Hello", name + ', ' + msg)

#Output -> Hello Rocky, Good morning!
hello("Rocky")
#Output -> Hello Alice, How do you do?
hello("Alice", "How do you do?")
```
**Arbitrary Arguments**

Sometimes, we do not know in advance the number of arguments that will be passed into a function.
Python allows us to handle this kind of situation through function calls with an arbitrary number of arguments.
We use `*` before the parameter name in this situation.
```python
def greet(*names):
    """This function greets all the person in the names tuple."""

    # names is a tuple with arguments
    for name in names:
        print("Hello", name)

# Output
# -> Hello Rocky
# -> Hello Luke
# -> Hello Alice
# -> Hello Annie
greet("Rocky", "Luke", "Alice", "Annie")
```
### 1.3 Lambda Functions (Anonymous Functions)
In Python, an `anonymous function` is a function that is `defined without a name`. While normal functions are defined 
using the `def` keyword in Python, anonymous functions are defined using the `lambda` keyword.

**Syntax**

```python
lambda arguments: expression
```
Lambda functions can have `any number of arguments` but `only one expression`.
The expression is evaluated and returned. Lambda functions can be used wherever function objects are required.
```python
double = lambda x: x * 2

# Equivalence with this method

def double(x):
   return x * 2
```
**Examples**
```python
# Script to filter out only the even items from a list
my_list = [1, 5, 4, 6, 8, 11, 3, 12]

new_list = list(filter(lambda x: (x%2 == 0) , my_list))

# Output -> [4, 6, 8, 12]
print(new_list)
```
```python
# Program to double each item in a list using map()

my_list = [1, 5, 4, 6, 8, 11, 3, 12]

new_list = list(map(lambda x: x * 2 , my_list))

# Output -> [2, 10, 8, 12, 16, 22, 6, 24]
print(new_list)
```
### 1.4 Variable Scopes
- Scope of a variable is the portion of a program where the variable is recognized.
Parameters and variables defined inside a function are not visible from outside the function.
Hence, they have a local scope.

- The lifetime of a variable is the period throughout which the variable exits in the memory.
The lifetime of variables inside a function is as long as the function executes.

- They are destroyed once we return from the function. 
Hence, a function does not remember the value of a variable from its previous calls.

**Global Scope**

In Python, a variable declared `outside of the function` or `in global scope` is known as a global variable.
This means that a global variable can be accessed inside or outside of the function.

**Local Scope**

A variable declared `inside the function's body` or in the local scope is known as a local variable.

_Example 1_
```python
a = 20

def my_function():
    a = 10
    print("Value inside function:", a)

my_function()
print("Value outside function:", a)

# Output
# -> Value inside function: 10
# -> Value outside function: 20
```
_Example 2_
```python
x = "global"

def double():
    x = x * 2
    print(x)

double()
# Output
# -> Error UnboundLocalError: local variable 'x' referenced before assignment
```
To fix the above issue we use `global` keyword
```python
x = 'global-'

def double():
    global x
    x = x * 2
    print(x)

# Output -> 'global-global-'
double()
# Output -> 'global-global-'
print(x)
```

> Be careful when use the global, nonlocal variables! Only use it when we really need it.
> And it should not be changed frequently.

**Nonlocal Scope**

Nonlocal variables are used `in nested functions` whose `local scope is not defined`.
This means that the variable can be neither in the `local` nor the `global` scope.
We use `nonlocal` keyword to classify the Nonlocal scope variable.
```python
x = "global"

def outer():
    x = "local"

    def inner():
        nonlocal x
        x = "nonlocal"
        print("inner:", x)

    inner()
    print("outer:", x)

# Output
# -> inner: nonlocal
# -> outer: nonlocal
outer()

# Output
# -> global: global
print("global:", x)
```
> Note : If we change the value of a nonlocal variable, the changes appear in the local variable.

## Session 2: Class & Object
### 2.1 Class & Object
The concept of `OOP in Python` focuses on creating reusable code.
This concept is also known as `DRY` (Don't Repeat Yourself).

We use the `class` keyword to define a class structure.

An `object` (instance) is an instantiation of a `class`. 
When `class is defined`, only the description for the object is defined.
Therefore, `no memory or storage is allocated`.
```python
class Husky:
    # class attributes
    species = 'dog'
    
    # instance attributes    
    def __init__(self, name, age, gender):
        """Constructor - called when the class object is initialized"""
        self.name = name
        self.age = age
        self.gender = gender
    
    # instance methods        
    def act(self, action):
        return "{} is trying to {}".format(self.name, action)
    
    def bark(self):
        return "{} is now barking".format(self.name)

doo = Husky('Doo', 6, 'Male')
daa = Husky('Daa', 4, 'Female')
# access the class attributes
print('Doo is a {}'.format(doo.__class__.species))
print('Daa is also a {}'.format(daa.__class__.species))

# access the instance attributes
print('{} is {} years old'.format(doo.name, doo.age))
print('{} is {} years old'.format(daa.name, daa.age))

# call our instance methods
print(doo.act("'Running around'"))
print(doo.bark())
```
### 2.2 OOP with Python Class
**Inheritance**

- We have two classes i.e. `Bird`(parent class) and `Penguin`(child class).
The child class inherits the functions of parent class. We can see this from the `swim()` method.

- The child class modified the behavior of the parent class.
We can see this from the `who_is_this()` and `fly()` method.
Furthermore, we extend the functions of the parent class, by creating a new `swim()` method.
```python
# parent class
class Bird:
    def __init__(self, name):
        self.name = name
        print(self.name, "is born.")

    def who_is_this(self):
        print(self.name, "is a 'Bird'.")

    def fly(self):
        print(self.name, "can fly.")

# child class
class Penguin(Bird):
    def __init__(self, name):
        # call super() function
        super().__init__(name)
        print("New penguin is born.")

    def who_is_this(self):
        print(self.name, "is a 'Penguin'.")

    def fly(self):
        print(self.name, "cannot fly.")

    def swim(self):
        print(self.name, "can swim.")


jacky = Penguin('Jacky')
jacky.who_is_this()
jacky.fly()
jacky.swim()
```
- Python supports `multiple inheritance`.
```python
class Base1:
    pass

class Base2:
    pass

class InheritedClass(Base1, Base2):
    pass
```
- Using `multiple inheritance` and `multilevel inheritance` can make our class structure become very complex.
This would cause many issues when maintaining them.
- There is another approach to  make the code reusable by using `Composition`.
- Composition means that an object knows another object, and explicitly delegates some tasks to it.
While `inheritance` is implicit, `composition` is explicit.
```python
class Door:
    def __init__(self, number, status):
        self.number = number
        self.status = status

    def open(self):
        self.status = 'open'

    def close(self):
        self.status = 'closed'


class SecurityDoor:
    locked = True

    def __init__(self, number, status):
        self.door = Door(number, status)

    def open(self):
        if self.locked:
            return
        self.door.open()

    def __getattr__(self, attr):
        return getattr(self.door, attr)


class ComposedDoor:
    def __init__(self, number, status):
        self.door = Door(number, status)

    def __getattr__(self, attr):
        return getattr(self.door, attr)


comp_door = ComposedDoor(1, 'open')
comp_door.open()
print('Composed Door Status:', comp_door.status)

sec_door = SecurityDoor(2, 'closed')
sec_door.open()
print('Security Door Status:', sec_door.status)
```

**Encapsulation**

- In Python, we denote private attributes using underscore as the prefix i.e single `_` or double `__`.
```python
class Bicycle:
    def __init__(self):
        self.__maxprice = 900

    def get_max_price(self):
        print("Selling Price: {}".format(self.__maxprice))

    def set_max_price(self, price):
        self.__maxprice = price


b = Bicycle()
b.get_max_price()

# change the price
b.__maxprice = 1000
b.get_max_price()

# using setter function
b.set_max_price(1000)
b.get_max_price()
```
**Polymorphism**
- Polymorphism is an ability (in OOP) to use a common interface for multiple forms (data types).
```python
class Bird:
    def __init__(self, name):
        self.name = name

    def fly(self):
        print(self.name, "can fly.")

    def swim(self):
        print(self.name, "can't swim.")


class Dove(Bird):
    def __init__(self, name):
        super().__init__(name)


class Penguin(Bird):
    def __init__(self, name):
        super().__init__(name)

    def fly(self):
        print(self.name, "can't fly.")

    def swim(self):
        print(self.name, "can swim.")


# common interface
def test_flying(bird):
    bird.fly()


# instantiate objects
peace = Dove('Peace')
jacky = Penguin('Jacky')

# passing the object
test_flying(peace)
test_flying(jacky)
```

**Abstract Base Classes**

- Python provided the `ABC` module (Abstract Base Classes) to support abstraction.
- We cannot instantiate an instance from an abstract class
-we are not required to implement do_something in the class defintition of B
```python
from abc import ABC, abstractmethod


class AbstractBird(ABC):
    def __int__(self):
        return

    @abstractmethod
    def fly(self):
        pass

    @abstractmethod
    def swim(self):
        pass

bird = AbstractBird()
# Output -> TypeError: Can't instantiate abstract class AbstractBird with abstract methods fly, swim
print(bird)
```
```python
from abc import ABC, abstractmethod


class AbstractBird(ABC):
    def __int__(self):
        return

    @abstractmethod
    def fly(self):
        pass

    @abstractmethod
    def swim(self):
        pass


class Penguin(AbstractBird):
    def __init__(self, name):
        self.name = name
        super().__init__()

    # def fly(self):
    #     print(self.name, "can't fly.")
    #
    # def swim(self):
    #     print(self.name, "can swim.")


jacky = Penguin('Jacky')
jacky.fly()
```
- We create `Penguin` class inherit from `AbstractBird` class. It will raise the warning that we should implement the 
`fly()` and `swim()` methods.
- We cannot instantiate the object from `Penguin` class as well until we implement the abstract methods.
new object.

```text
Key Points to Remember:
- Object-Oriented Programming makes the program easy to understand as well as efficient.
- Since the class is sharable, the code can be reused.
- Data is safe and secure with data abstraction.
- Polymorphism allows the same interface for different objects, so programmers can write efficient code.```
