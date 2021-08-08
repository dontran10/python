import datetime
from enum import Enum

class ParkTimeRange(Enum) :
    DAY_LIGHT = 1
    BEFORE_MIDNIGHT = 2
    AFTER_MIDNIGHT = 3

#
#Return the next weekday (0: Monday, 1: Tuesday....6: Sunday)
#
def getNexWeekday(weekday):
    weekday = weekday + 1
    if weekday > 6:
        weekday = 0
    return weekday

def getHourRangeWeekday(ptime):
    hour = int(ptime.strftime("%H"))
    weekday = ptime.weekday()
    if (hour >= 8) and (hour < 17):
        return ParkTimeRange.DAY_LIGHT, weekday,hour
    elif (hour >= 17) and (hour <= 23):
        return ParkTimeRange.BEFORE_MIDNIGHT, weekday,hour
    else:
        return ParkTimeRange.AFTER_MIDNIGHT, weekday,hour

def calculateFeeInRange(parkingHours, weekday, range):
    maxHour = 0
    pricePerHour = 0
    discount = 0
     
    if (range == ParkTimeRange.DAY_LIGHT):
        # Monday to Friday
        if (weekday >= 0) and (weekday <= 4):
            maxHour = 2
            pricePerHour = 10
            discount = 10
        # Saturday
        elif weekday == 5:
            maxHour = 4
            pricePerHour = 3
            discount = 10
        # Sunday
        else:
            maxHour = 8
            pricePerHour = 2
            discount = 10
    elif (range == ParkTimeRange.BEFORE_MIDNIGHT):
        maxHour = 7
        pricePerHour = 5
        discount = 50
    else:
        maxHour = 8
        pricePerHour = 20
        discount = 10
    fee = 0
    exceedHours = parkingHours - maxHour
    if(parkingHours <=0 ):
        fee = 0
    elif exceedHours <= 0:
        fee = parkingHours*pricePerHour
    else:
        fee = maxHour*pricePerHour + exceedHours*pricePerHour*2
    fee = fee* (100 - discount)/100

    return fee


def calculateParkingFee(strParkTime, strPickTime, timeFormat):
    parkTime = datetime.datetime.strptime(strParkTime, timeFormat)
    pickTime = datetime.datetime.strptime(strPickTime, timeFormat)
    
    
    packDurationInHour = (pickTime - parkTime).total_seconds() / 3600
    packDurationInDay =  int((packDurationInHour // 24) - 1)
   
    fee = 0
    arrivalRange, arrivalWeekday, arrivalHour = getHourRangeWeekday(parkTime)
    pickRange, pickWeekday, pickHour = getHourRangeWeekday(pickTime)

    # First calculate fee for (a part) of arrival day and (a part) of pick day
    # Arrival day and pick day can be same day or pick day is a day after arrival day 
    if arrivalRange == ParkTimeRange.DAY_LIGHT:

        duration1 = 0
        duration2 = 0
        duration3 = 0 
        if (pickHour >= 8) and (pickHour < 17):
            duration1 = 17 - arrivalHour + 1            
        elif (pickHour >= 17) and (pickHour < 23):
            duration1 = 17 - arrivalHour 
            duration2 = pickHour - 17 + 1

        elif (pickHour >= 0) and (pickHour < 8):
            duration1 = 17 - arrivalHour
            duration2 = 7
            duration3 = pickHour + 1
        
        fee = calculateFeeInRange(duration1, arrivalWeekday,ParkTimeRange.DAY_LIGHT) \
            + calculateFeeInRange(duration2, arrivalWeekday,ParkTimeRange.BEFORE_MIDNIGHT) \
            + calculateFeeInRange(duration3, pickWeekday,ParkTimeRange.AFTER_MIDNIGHT) \
            + calculateFeeInRange(pickHour - 8 , pickWeekday,ParkTimeRange.DAY_LIGHT)
    elif arrivalRange == ParkTimeRange.BEFORE_MIDNIGHT:

        duration1 = 0
        duration2 = 0
        duration3 = 0 
        if (pickHour >= 17) and (pickHour < 23):
            duration2 = 23 - arrivalHour + 1             
        elif (pickHour >= 0) and (pickHour < 8):
            duration2 = 23 - arrivalHour 
            duration3 = pickHour + 1

        elif (pickHour >= 8) and (pickHour < 17):
            duration2 = 23 - arrivalHour
            duration3 = 8
            duration1 = pickHour -8 + 1
        
        fee = calculateFeeInRange(duration2, arrivalWeekday,ParkTimeRange.BEFORE_MIDNIGHT) \
            + calculateFeeInRange(duration3, pickWeekday,ParkTimeRange.AFTER_MIDNIGHT) \
            + calculateFeeInRange(duration1, pickWeekday,ParkTimeRange.DAY_LIGHT) \
            + calculateFeeInRange(pickHour - 17 + 1, pickWeekday,ParkTimeRange.BEFORE_MIDNIGHT)
        
    elif arrivalRange == ParkTimeRange.AFTER_MIDNIGHT:

        duration1 = 0
        duration2 = 0
        duration3 = 0 
        if (pickHour >= 0) and (pickHour < 8):
            duration3 = pickHour - arrivalHour + 1             
        elif (pickHour >= 8) and (pickHour < 17):
            duration3 = 8 - arrivalHour 
            duration1 = pickHour - 8 + 1

        elif (pickHour >= 17) and (pickHour < 23):
            duration3 = 8 - arrivalHour 
            duration1 = 9
            duration2 = pickHour - 17 + 1
        
        fee = calculateFeeInRange(duration3, arrivalWeekday,ParkTimeRange.AFTER_MIDNIGHT) \
            + calculateFeeInRange(duration1, arrivalWeekday,ParkTimeRange.DAY_LIGHT) \
            + calculateFeeInRange(duration2, arrivalWeekday,ParkTimeRange.BEFORE_MIDNIGHT) \
            + calculateFeeInRange(8 - pickHour, pickWeekday,ParkTimeRange.AFTER_MIDNIGHT)

    # Second, add fee to fee of whole day * n (days) (n days between arrival day and pick day)
    nextWeekDay = getNexWeekday(arrivalWeekday)
    for d in range(packDurationInDay):
        fee = fee + calculateFeeInRange(8, nextWeekDay,ParkTimeRange.AFTER_MIDNIGHT) \
            + calculateFeeInRange(9, nextWeekDay,ParkTimeRange.DAY_LIGHT) \
            + calculateFeeInRange(7, nextWeekDay,ParkTimeRange.BEFORE_MIDNIGHT) 
        nextWeekDay = getNexWeekday(nextWeekDay)
    
    # Round up with two decimal
    return round(fee, 2)


