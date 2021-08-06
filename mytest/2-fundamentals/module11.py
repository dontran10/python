def checkDigitCalculation(digits):
    if digits.isdigit():
        addsum = sum((len(digits) + 1 - pos)*int(num) for pos,num in enumerate(digits))
        check_digit = 11 - (addsum % 11)
        return digits + str(check_digit)
    else:
        return None
    