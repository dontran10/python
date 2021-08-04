import math
def find_angle_MBC(ab, bc):
    # TODO: Enjoy your math solving here
    # Hint: We should math library in Python for this labd
    if (a <= 0 or a > 100) or (b <= 0 or b > 100):
        raise Exception('Invalid input, value must be 0 < x <= 100')
    else:
        c = math.sqrt(a**2 + b**2)
        radian = math.asin(a/c)
        return round(math.degrees(radian))

if __name__ == '__main__':
    a, b = int(input()), int(input())    
    print(find_angle_MBC(a, b))
