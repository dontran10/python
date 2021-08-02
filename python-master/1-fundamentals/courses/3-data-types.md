# Module 3: Datatypes
## Session 1: Python Numbers
### 1.1 Number Datatype
Python support integers, floating-point numbers, and complex numbers.
They are defined as `int`, `float`, `complex` classes.
~~~
floating-point number is accurate only up to 15 decimal places (the 16th place is inaccurate).
~~~
We can use `type()` to know which class a variable/value belongs to and `isinstance()` to check if it belongs to a 
particular class.
```python
a = 5
b = 5.0
# Output -> <class 'int'>
print(type(a))
# Output -> <class 'float'>
print(type(b))
```
```python
c = 2 + 3j
# Output -> True
print(isinstance(c, complex))
```
Operations like `+`, `-`, `*`, `/` coerce `integer` to `float` implicitly (automatically), if one of the operands is `float`.
```python
# Output -> 3.1
print(1 + 2.1) 

# Output -> 6.300000000000001
print(2.1 * 3)
```
### 1.2 Type Conversion
We can convert one type of number into another. This is also known as coercion.
The built-in functions like `int()`, `float()` and `complex()` is used to convert between types explicitly.
These functions can even convert from `strings`.
```python
# Output -> 2
int(2.3)

# Output -> -2
int(-2.8) 

# Output -> 2
int('2')

# Output -> 5.0
float(5)

# Output -> 2.5
float('2.5')
```
### 1.3 Python Decimal
Let 's try this sample:
```python
# Output -> 3.3000000000000003 ?!?
print(float('1.1') + float('2.2'))
```
It turns out that floating-point numbers are implemented in computer hardware as binary fractions as the computer only 
understands binary (0 and 1).
Due to this reason, most of the decimal fractions we know, cannot be accurately stored in our computer.

Another example, we cannot represent the fraction `1/3` as a correct decimal number. It will give an infinitely long 
number `0.33333333333...`.

To overcome this issue, we use `decimal module`. While floating-point numbers have precision up to 15 decimal places, 
the decimal module has user-settable precision.
```python
from decimal import Decimal

# Output -> 3.3
print(Decimal('1.1') + Decimal('2.2'))
```
It also preserves significance.
We know `25.50` is more accurate than `25.5` as it has two significant decimal places compared to one.
(_**Notice the trailing zeroes in the below example**_)
```python
from decimal import Decimal

# Output -> 3.000
print(Decimal('1.2') * Decimal('2.50'))
```
**When to use Decimal instead of float?**
- When we are making financial applications that need exact decimal representation.
- When we want to control the level of precision required.
- When we want to implement the notion of significant decimal places.
### 1.4 Python Fractions
Python provides operations involving fractional numbers through its `fractions module`.
```python
import fractions

# Output -> 3/2
print(fractions.Fraction(1.5))
# Output -> 5
print(fractions.Fraction(5))
# Output -> 1/3
print(fractions.Fraction(1, 3))
```
While creating `Fraction` from `float`, we might get some unusual results.
This is due to the `imperfect binary floating point` number representation as discussed in the previous section.

Fortunately, `Fraction` allows us to instantiate with `string` as well.
This is the preferred option when using decimal numbers.
```python
import fractions

# Output as float -> 2589569785738035/2251799813685248
print(fractions.Fraction(1.15))

# Output as string -> 23/20
print(fractions.Fraction('1.15'))
```
### 1.5 Python Mathematics
Python offers modules like `math` and `random` to carry out different `mathematics` like `trigonometry`, `logarithms`, 
`probability` and `statistics`, etc.
```python
import math

# Output PI number -> 3.14..
print(math.pi)

# Output cos of a 60° angle -> 0.5 
print(math.cos(math.radians(60)))

# Output e^10
print(math.exp(10))

# Output log10 of 1000 -> 3
print(math.log10(1000))

# Output of 4! -> 1*2*3*4 = 24
print(math.factorial(4))
```
```python
import random
# Get random number in range

print(random.randrange(10, 20))

x = ['a', 'b', 'c', 'd', 'e']
# Get random choice
print(random.choice(x))
# Shuffle x
random.shuffle(x)
# Print the shuffled x
print(x)

# Print random element
print(random.random())
```
## Session 2: Python List
Python offers a range of compound data types often referred to as sequences.
`List` is one of the most frequently used and very versatile data types used in Python.
### 2.1 How to create a list?
In Python programming, a `list` is created by placing all the items (elements) inside square brackets `[]`,
separated by commas.

It can have any number of items and they may be of different types (`integer`, `float`, `string` etc.).
```python
# empty list
my_list = []

# list of integers
my_list = [1, 2, 3]

# list with mixed data types
my_list = [1, "Hello", 3.4]

# nested list
my_list = ["mouse", [8, 4, 6], ['a']]
```
### 2.2 How to access elements from a list?
**Using List Index**
```python
# List indexing
my_list = ['p', 'y', 't', 'h', 'o', 'n']

# Output -> p
print(my_list[0])

# Output -> t
print(my_list[2])

# Output -> o
print(my_list[4])

# Nested List
n_list = ["Happy Learning", [2, 0, 2, 0]]

# Nested indexing
# Output -> a
print(n_list[0][1])

# Output -> 0
print(n_list[1][3])
```
**Using Negative Index**
```python
# Negative indexing in lists
# Index value  [-6, -5, -4, -3, -2, -1]
my_list = ['p', 'y', 't', 'h', 'o', 'n']

# Output -> n
print(my_list[-1])

# Output -> y
print(my_list[-5])
```
### 2.3 How to slice lists in Python?
We can access a range of items in a list by using the slicing operator `:`(colon).
```python
# List slicing in Python

my_list = ['N', 'A', 'S', 'H', 'T', 'E', 'C', 'H']

# Output elements 5rd to 8th
# -> ['T', 'E', 'C', 'H']
print(my_list[4:8])

# Output elements from beginning to 4th 
# -> ['N', 'A', 'S', 'H']
print(my_list[:-4])

# Output elements 5th to end
# -> ['T', 'E', 'C', 'H']
print(my_list[4:])

# Output elements beginning to end
# -> ['N', 'A', 'S', 'H', 'T', 'E', 'C', 'H']
print(my_list[:])
```
### 2.4 How to change or add elements to a list?
Lists are `mutable`, meaning their elements can be changed unlike `string` or `tuple`.

We can use the assignment operator (`=`) to change an item or a range of items.
```python
my_list = [0, 2, 4, 6, 8]

# Change the 1st item    
my_list[0] = 1            

# Output -> [1, 2, 4, 6, 8]
print(my_list)

# change 2nd to 5th items
my_list[1:5] = [3, 5, 7, 9]

# Output -> [1, 3, 5, 7, 9]
print(my_list)
```
We can add one item to a list using the `append()` method or add several items using `extend()` method.

We can reverse the order of items in the list using `reverse()` method.
```python
my_list = [1, 3, 5, 7, 9]
my_list.append(11)

# Output -> [1, 3, 5, 7, 9, 11]
print(my_list)

my_list.extend([13, 15])

# Output -> [1, 3, 5, 7, 9, 11, 13, 15]
print(my_list)

my_list.reverse()
# Output -> [15, 13, 11, 9, 7, 5, 3, 1]
print(my_list)
```
We can also use `+` operator to combine two lists.
```python
my_list = [0, 2, 4]

# Output -> [0, 2, 4, 6, 8]
print(my_list + [6, 8])
```
The `*` operator repeats a list for the given number of times.
```python
# Output -> ['Get Ready', 'Get Ready', 'Get Ready']
print(['Get Ready'] * 3)
```
We can insert one item at a desired location by using the method `insert()` or insert multiple items by squeezing 
it into an empty slice of a list.
```python
my_list = [0, 8, 10]

# Insert '2' into position 1, other items will be right shifted.
my_list.insert(1, 2)

# Output -> [0, 2, 8, 10]
print(my_list)

my_list[2:2] = [4, 6]

# Output -> [0, 2, 4, 6, 8, 10]
print(my_list)
```
### 2.5 How to delete or remove elements from a list?
We can delete one or more items from a list using the keyword `del`. It can even delete the list entirely.

We can use `remove()` method to remove the given item or `pop()` method to remove an item at the given index.

The `pop()` method removes and returns the last item if the index is not provided.
This helps us implement lists as stacks (first in, last out data structure).

We can also use the `clear()` method to empty a list.

```python
my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
my_list.remove(5)

# Output -> [0, 1, 2, 3, 4, 6, 7, 8, 9]
print(my_list)

# Output -> 1
print(my_list.pop(1))

# Output: [0, 2, 3, 4, 6, 7, 8, 9]
print(my_list)

# Output -> 9
print(my_list.pop())

# Output -> [0, 2, 3, 4, 6, 7, 8]
print(my_list)

my_list.clear()

# Output -> []
print(my_list)
```
## Session 3: Python Tuple
A `tuple` is created by placing all the items (elements) inside parentheses `()`, separated by `commas`.

A `tuple` can have any number of items and they may be of different types (`integer`, `float`, `list`, `string`, etc.).

We can interact with `tuple` the same way we do with a `list`. The main difference thing is tuple is `immutable`.
This means that elements of a tuple cannot be changed once they have been assigned.
But, if the element is itself a mutable data type like list, its nested items can be changed.

```python
my_tuple = (1 ,2 ,3 , ['a', 'b'])

# TypeError: 'tuple' object does not support item assignment
# my_tuple[1] = 0

# Item of mutable element can be changed
my_tuple[3][0] = 'a1'

# Output -> (1, 2, 3, ['a1', 'b'])
print(my_tuple)

# Tuples can be reassigned
my_tuple = ('N', 'A', 'S', 'H', 'T', 'E', 'C', 'H')

# Output -> ('N', 'A', 'S', 'H', 'T', 'E', 'C', 'H')
print(my_tuple)

# Concatenation
# Output -> (1, 2, 3, 4, 5, 6)
print((1, 2, 3) + (4, 5, 6))

# Repeat
# Output -> ('Practice', 'Practice', 'Practice')
print(('Practice',) * 3)

# Can delete an entire tuple
del my_tuple

# NameError: name 'my_tuple' is not defined
print(my_tuple)
```

**Advantages of Tuple over List**

Since `tuples` are quite similar to `lists`, both of them are used in similar situations.
However, there are certain advantages of implementing a tuple over a list:
- We generally use `tuples` for `different data types` and `lists` for `similar data types`.
- Since tuples are `immutable`, iterating through a tuple is faster than with list.
So there is a slight performance boost.
- Tuples that contain `immutable elements` can be used as a `key for a dictionary`. With lists, this is not possible.
- If you have `data that doesn't change`, implementing it as tuple will guarantee that it remains` write-protected`.
## Session 4: Python String
### 4.1 How to create a string in Python?
```python
# Defining strings in Python
# All of the following are equivalent
my_string = 'Hello'
print(my_string)

my_string = "Hello"
print(my_string)

my_string = '''Hello'''
print(my_string)

# Triple quotes string can extend multiple lines
my_string = """Hello, welcome to
           the world of Python"""
print(my_string)
```
### 4.2 How to access characters in a string?
We can access characters in a string using `indexing` or `:`(slice) like we do with `list` and `tuple`.
Python also allows `negative indexing` for string as well.

We can get string length by using `len()` method.

String is `immutable`, so we CANNOT change/delete string characters.

We can concatenate(`+`) or generate repeated string (`*`) as well.
```python
str1 = 'Python'
str2 = ' is '
str3 = 'fun'
# Output -> 'Python is fun'
print(str1 + str2 + str3)

# Output -> 'PythonPythonPython'
print(str1 * 3)
```
## Session 5: Python Set
A `set` is an `unordered collection of items`. `Every` set `element` is `unique` (no duplicates) and must be `immutable` 
(cannot be changed).

However, a `set` itself `is` `mutable`. We can add or remove items from it.

Sets can also be used to perform mathematical set operations like union, intersection, symmetric difference, etc.
### 5.1 Creating Python Sets
A set is created by placing all the items (elements) inside curly braces `{}`, separated by `comma`, 
or by using the built-in `set()` function.

It can `have` any number of items and they may be of different types (`integer`, `float`, `tuple`, `string` etc.). 
But a set `cannot have` mutable elements like `lists`, `sets` or `dictionaries` as its elements.

```python
# Different types of sets in Python
# set of integers
my_set = {1, 2, 3}
print(my_set)

# set of mixed data types
my_set = {1.0, "Hello", (1, 2, 3)}
print(my_set)
```
### 5.2 Modifying a set in Python
Sets are `mutable`. However, since they are `unordered`, indexing has no meaning.

We cannot access or change an element of a set using `indexing` or `slicing`. Set data type does not support it.`

We can add a single element using the `add()` method, and multiple elements using the `update()` method.
The `update()` method can take `tuples`, `lists`, `strings` or other sets as its argument. 
In all cases, duplicates are avoided.
```python
my_set = {1, 3}
# Output -> {1, 3}
print(my_set)

# Add an element
my_set.add(2)
# Output -> {1, 2, 3}
print(my_set)

# Add multiple elements
my_set.update([2, 3, 4])
# Output: {1, 2, 3, 4}
print(my_set)

# Add list and set
my_set.update([4, 5], {1, 6, 8})
# Output -> {1, 2, 3, 4, 5, 6, 8}
print(my_set)
```
### 5.3 Removing elements from a set
A particular item can be removed from a `set` using the methods `discard()` and `remove()`:
- `discard()` function leaves a set unchanged if the element is not present in the set.
- `remove()` function will raise an error in such a condition (if element is not present in the set).
```python
# Difference between discard() and remove()

# initialize my_set
my_set = {1, 3, 4, 5, 6}
print(my_set)

# discard an element
# Output -> {1, 3, 5, 6}
my_set.discard(4)
print(my_set)

# remove an element
# Output -> {1, 3, 5}
my_set.remove(6)
print(my_set)

# discard an element
# not present in my_set
# Output -> {1, 3, 5}
my_set.discard(2)
print(my_set)

# remove an element
# not present in my_set
# you will get an error.
# Output -> KeyError
my_set.remove(2)
```
### 5.4 Python Set Operations
**Set Union**

Union of `A` and `B` is a set of all elements from both sets.

Union is performed using `|` operator. Same can be accomplished using the `union()` method.
```python
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

# use | operator
# Output -> {1, 2, 3, 4, 5, 6, 7, 8}
print(A | B)

# use union function
# Output -> {1, 2, 3, 4, 5, 6, 7, 8}
print(A.union(B))

# use union function on B
# Output -> {1, 2, 3, 4, 5, 6, 7, 8}
print(B.union(A))
```
**Set Intersection**

Intersection of `A` and `B` is a set of elements that are common in both the sets.

Intersection is performed using `&` operator. Same can be accomplished using the `intersection()` method.
```python
# Intersection of sets
# initialize A and B
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

# use & operator
# Output -> {4, 5}
print(A & B)

# use intersection function on A
# Output -> {4, 5}
print(A.intersection(B))

# use intersection function on B
# Output -> {4, 5}
print(B.intersection(A))
```
**Set Difference**

Difference of the set `B` from set `A`(`A` - `B`) is a set of elements that are only in `A` but not in `B`.
Similarly, `B` - `A` is a set of elements in `B` but not in `A`.

Difference is performed using `-` operator. Same can be accomplished using the `difference()` method.
```python
# Difference of two sets
# initialize A and B
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

# use - operator on A
# Output -> {1, 2, 3}
print(A - B)
# use - operator on B
# Output -> {8, 6, 7}
print(B - A)

# use difference function on A
# Output -> {1, 2, 3}
print(A.difference(B))
# use difference function on B
# Output -> {8, 6, 7}
print(B.difference(A))
```
**Set Symmetric Difference**

Symmetric Difference of `A` and `B` is a set of elements in `A` and `B` but not in both (excluding the intersection).

Symmetric difference is performed using `^` operator. Same can be accomplished using the method symmetric_difference().
```python
# Symmetric difference of two sets
# initialize A and B
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

# use ^ operator
# Output -> {1, 2, 3, 6, 7, 8}
print(A ^ B)

# use symmetric_difference function on A
# Output -> {1, 2, 3, 6, 7, 8}
print(A.symmetric_difference(B))

# use symmetric_difference function on B
# Output -> {1, 2, 3, 6, 7, 8}
print(B.symmetric_difference(A))
```
## Session 6: Python Dictionary
Python dictionary is an unordered collection of items. Each item of a dictionary has a `key/value` pair.

Dictionaries are `optimized to retrieve values` when the `key is known`.
### 6.1 Creating Python Dictionary
Creating a dictionary is as simple as placing items inside curly braces `{}` separated by `commas`.
We can also create a dictionary using the built-in `dict()` function.

An item has a key and a corresponding value that is expressed as a pair (**key: value**).
```python
# empty dictionary
my_dict = {}

# dictionary with integer keys
my_dict = {1: 'apple', 2: 'ball'}

# dictionary with mixed keys
my_dict = {'name': 'John', 1: [2, 4, 3]}

# using dict()
my_dict = dict({1:'apple', 2:'ball'})

# from sequence having each item as a pair
my_dict = dict([(1,'apple'), (2,'ball')])
```
### 6.2 Accessing Elements from Dictionary
While indexing is used with other data types to access values, a dictionary uses keys.

Keys can be used either inside square brackets `[]` or with the `get()` method:
- Using `[]`, `KeyError` is raised in case a key is not found in the dictionary.
- Using `get()` returns `None` if the key is not found.
```python
# get vs [] for retrieving elements
my_dict = {'name': 'Rocky', 'age': 18}

# Output -> Rocky
print(my_dict['name'])

# Output -> 18
print(my_dict.get('age'))

# Trying to access keys which doesn't exist throws error
# Output None
print(my_dict.get('address'))

# KeyError
print(my_dict['address'])
```
### 6.3 Changing and Adding Dictionary elements
Dictionaries are mutable. We can add new items or change the value of existing items using an assignment operator.

If the key is already present, then the existing value gets updated.
In case the key is not present, a new (**key: value**) pair is added to the dictionary.
```python
# Changing and adding Dictionary Elements
my_dict = {'name': 'Rocky', 'age': 18}

# update value
my_dict['age'] = 24

#Output -> {'age': 24, 'name': 'Rocky'}
print(my_dict)

# add item
my_dict['address'] = 'Vietnam'

# Output -> {'address': 'Vietnam', 'age': 24, 'name': 'Rocky'}
print(my_dict)
```
### 6.4 Removing elements from Dictionary
We can remove a particular item in a dictionary by using the `pop()` method.
This method removes an item with the provided key and returns the value.

The `popitem()` method can be used to remove and return an arbitrary (key, value) item pair from the dictionary.

All the items can be removed at once, using the `clear()` method.

We can also use the `del` keyword to remove individual items or the entire dictionary itself.
```python
# Removing elements from a dictionary

# create a dictionary
squares = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# remove a particular item, returns its value
# Output -> 16
print(squares.pop(4))

# Output -> {1: 1, 2: 4, 3: 9, 5: 25}
print(squares)

# remove an arbitrary item, return (key,value)
# Output -> (5, 25)
print(squares.popitem())

# Output -> {1: 1, 2: 4, 3: 9}
print(squares)

# remove all items
squares.clear()

# Output -> {}
print(squares)

# delete the dictionary itself
del squares

# Throws Error
print(squares)
```
[**Back to Module List**](../README.md)