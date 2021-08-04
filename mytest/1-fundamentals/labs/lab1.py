def is_leap(year):
    leap = False
    if (year < 1900) or (year > 10**5):
        raise Exception('Invalid year, must between 1900 and 10^5')
    else:
        leap =  (year % 4 == 0) and ((year % 100 != 0) or (year % 400 == 0))
    return leap

if __name__ == '__main__':
    y = int(input("Enter a year:"))
    print(is_leap(y))