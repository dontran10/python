# Module 4: Date and Time

## Session 1: Python datetime, date, time Module
- Python has a module named `datetime`, `date`, and `time` to work with dates and times.
- **Sample for datetime**
```python
from datetime import datetime

# Get current date + time
a = datetime.now()
print(a)

# datetime(year, month, day)
b = datetime(2018, 11, 28)
print(b)

# datetime(year, month, day, hour, minute, second, microsecond)
c = datetime(2017, 11, 28, 23, 55, 59, 342380)
print(c)
print("year =", c.year)
print("month =", c.month)
print("hour =", c.hour)
print("minute =", c.minute)
print("timestamp =", c.timestamp())

# Get current timestamp & get date from timestamp
current_timestamp = datetime.today().timestamp()
print(datetime.fromtimestamp(current_timestamp))
```
- **Sample for date**
```python
from datetime import date
# Get current date
a = date.today()
print(a)

# Generate date object with format (year, month, day)
b = date(2020, 6, 1)
print(b)

# Get today's year, month, and day
today = date.today()
print("Current year:", today.year)
print("Current month:", today.month)
print("Current day:", today.day)
```
- **Sample for time**
```python
from datetime import time

# time(hour = 0, minute = 0, second = 0)
a = time()
print("a =", a)

# time(hour, minute and second)
b = time(11, 34, 56)
print("b =", b)

# time(hour, minute and second)
c = time(hour=11, minute=34, second=56)
print("c =", c)

# time(hour, minute, second, microsecond)
d = time(11, 34, 56, 234566)
print("d =", d)
print("hour =", d.hour)
print("minute =", d.minute)
print("second =", d.second)
print("microsecond =", d.microsecond)
```
- **Python timedelta**: A `timedelta` object represents the difference between two `dates` or `times`.
```python
from datetime import datetime, date

t1 = date(year=2019, month=6, day=18)
t2 = date(year=2018, month=6, day=19)
t3 = t1 - t2
print("t3 =", t3)

t4 = datetime(year=2019, month=6, day=18, hour=13, minute=30, second=0)
t5 = datetime(year=2020, month=6, day=18, hour=13, minute=30, second=30)
t6 = t4 - t5
print("t6 =", t6)

print("type of t3 =", type(t3))
print("type of t6 =", type(t6))
```
## Python datetime formatting
Python has `strftime()` and `strptime()` methods to handle the datetime formatting.

**Python strftime() - datetime object to string**

The `strftime()` method is defined under classes `date`, `datetime` and `time`.
The method creates a formatted string from a given `date`, `datetime` or `time` object.
```python
from datetime import datetime

# current date and time
now = datetime.now()

t = now.strftime("%H:%M:%S")
print("time:", t)

s1 = now.strftime("%m/%d/%Y, %H:%M:%S")
# mm/dd/YY H:M:S format
print("s1:", s1)

s2 = now.strftime("%d/%m/%Y, %H:%M:%S")
# dd/mm/YY H:M:S format
print("s2:", s2)
```
**Python strptime() - string to datetime**
The strptime() method creates a datetime object from a given string (representing date and time).
```python
from datetime import datetime

date_string = "21 June, 2018"
print("date_string =", date_string)

# The strptime() method takes two arguments:
# 1. a string representing date and time
# 2. format code equivalent to the first argument
date_object = datetime.strptime(date_string, "%d %B, %Y")
print("date_object =", date_object)
```
If the string (first argument) and the format code (second argument) passed to the `strptime()` doesn't match, 
you will get `ValueError`.
```python
from datetime import datetime

date_string = "18/06/2020"
date_object = datetime.strptime(date_string, "%d %m %Y")

# Output -> ValueError: time data '18/06/2020' does not match format '%d %m %Y'
print("date_object =", date_object)
```

The table below shows all the codes that we can use for formatting:

| Directive | Meaning | Example |
|:---: | --- | --- |
| `%a` | Abbreviated weekday name. | Sun, Mon, ... |
| `%A` | Full weekday name. | Sunday, Monday, ... |
| `%w` | Weekday as a decimal number. | 0, 1, ..., 6 |
| `%d` | Day of the month as a zero-padded decimal. | 01, 02, ..., 31 |
| `%-d` | Day of the month as a decimal number. | 1, 2, ..., 30 |
| `%b` | Abbreviated month name. | Jan, Feb, ..., Dec |
| `%B` | Full month name. | January, February, ... |
| `%m` | Month as a zero-padded decimal number. | 01, 02, ..., 12 |
| `%-m` | Month as a decimal number. | 1, 2, ..., 12 |
| `%y` | Year without century as a zero-padded decimal number. | 00, 01, ..., 99 |
| `%-y` | Year without century as a decimal number. | 0, 1, ..., 99 |
| `%Y` | Year with century as a decimal number. | 2013, 2019 etc. |
| `%H` | Hour (24-hour clock) as a zero-padded decimal number. | 00, 01, ..., 23 |
| `%-H` | Hour (24-hour clock) as a decimal number. | 0, 1, ..., 23 |
| `%I` | Hour (12-hour clock) as a zero-padded decimal number. | 01, 02, ..., 12 |
| `%-I` | Hour (12-hour clock) as a decimal number. | 1, 2, ... 12 |
| `%p` | Locale’s AM or PM. | AM, PM |
| `%M` | Minute as a zero-padded decimal number. | 00, 01, ..., 59 |
| `%-M` | Minute as a decimal number. | 0, 1, ..., 59 |
| `%S` | Second as a zero-padded decimal number. | 00, 01, ..., 59 |
| `%-S` | Second as a decimal number. | 0, 1, ..., 59 |
| `%f` | Microsecond as a decimal number, zero-padded on the left. | 000000 - 999999 |
| `%z` | UTC offset in the form +HHMM or -HHMM. | | 	 
| `%Z` | Time zone name. |  |
| `%j` | Day of the year as a zero-padded decimal number. | 001, 002, ..., 366 |
| `%-j` | Day of the year as a decimal number. | 1, 2, ..., 366 |
| `%U` | Week number of the year (Sunday as the first day of the week). | 00, 01, ..., 53 |
| `%W` | Week number of the year (Monday as the first day of the week). | 00, 01, ..., 53 |
| `%c` | Locale’s appropriate date and time representation. | Mon Sep 30 07:06:05 2013 |
| `%x` | Locale’s appropriate date representation. | 09/30/13 |
| `%X` | Locale’s appropriate time representation. | 07:06:05 |
| `%%` | A literal '%' character. | % |

**Handling timezone in Python**

Rather than trying to handle timezone ourselves, we should use a common 3rd-party `pytZ` module.
```python
from datetime import datetime
import pytz

local = datetime.now()
print("Local:", local.strftime("%m/%d/%Y, %H:%M:%S"))

tz_NY = pytz.timezone('America/New_York')
datetime_NY = datetime.now(tz_NY)
print("New York:", datetime_NY.strftime("%m/%d/%Y, %H:%M:%S"))

tz_London = pytz.timezone('Europe/London')
datetime_London = datetime.now(tz_London)
print("London:", datetime_London.strftime("%m/%d/%Y, %H:%M:%S"))
```