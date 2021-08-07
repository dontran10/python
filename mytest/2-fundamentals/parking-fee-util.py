import datetime
import re
import string
import json
import os

def calculateParkingFee(strParkTime, strPickTime, timeFormat):
    parkTime = datetime.datetime.strptime(strParkTime, timeFormat)
    pickTime = datetime.datetime.strptime(strParkTime, timeFormat)
    hour = parkTime.strftime("%H")
    weekday = parkTime.weekday() #Monday =0
    packDurationInMinutes = (pickTime - parkTime).total_seconds() / 60

    # Monday to Friday 
    if (weekday) >= 0) and (weekday <= 4): 

    if (hour >=8) and (hour < 17) :

   

    return 0
