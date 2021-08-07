import datetime
import re
import string
import json

class ParkingInfo:
    dt_format = '%Y-%m-%d %H:%M'
    ##
    car_identity = ""
    arrival_time = ""
    frequency_number = ""

    def __init__(self):
        pass
  
    def getCurrentTime():
        return datetime.datetime.now().strftime(ParkingInfo.dt_format)

    def isValidParkTime( strtime):
        isValid = True
        try:
            datetime.datetime.strptime(strtime, ParkingInfo.dt_format)
        except Exception:
            isValid = False
        return 
        
    def isValidCarIdentity(id):
        p = re.compile("^[0-9]{2}[A-Z]{1}[-]{1}[0-9]{5}$")
        return p.match(id)
    
    def isValidFrequencyNumber(digits):
        digits = digits.strip()
        if digits.isdigit() and (len(digits) == 5):
            origin = digits[: 4]
            addsum = sum((len(origin) + 1 - pos)*int(num) for pos,num in enumerate(origin))
            check_digit = 11 - (addsum % 11)
            return int(digits[4:]) == check_digit
        else:
            return False

    def inputPackingInfo(self) :
         # Arrival Time
        while True:
            self.arrival_time = str(input('Arrival Time (enter to get current time):'))
            if len(self.arrival_time) == 0:
                self.arrival_time = ParkingInfo.getCurrentTime()
                break
            elif ParkingInfo.isValidParkTime(self.arrival_time):
                break
            else:
                print('Invalid datetime (yyy-MM-dd hh:mm), re-enter gain')
        # Car IdentitY
            self.car_identity = str(input('Car Identity (ex: 01A-12345):'))
            if ParkingInfo.isValidCarIdentity(self.car_identity):
                break
            else:
                print('Invalid identiy, re-enter gain')
        
        # Frequency Number
            self.frequency_number = str(input('Frequency Number (ex: 12343):'))
            if ParkingInfo.isValidFrequencyNumber(self.frequency_number):
                break
            else:
                print('Invalid frequencey number, re-enter gain')
    
    def saveParkingInfo(self):
        appendData = {}
        appendData['parking-info'] = []
        appendData['parking-info'].append({
            'car-identity': self.car_identity,
            'datetime': self.arrival_time,
            'frequency-number': self.frequency_number,
            'operation': 'PARK'
        })

        data = None
        fullname = ".\\parking-data\\parking\\" + self.car_identity + ".json"
        with open(fullname , "a+") as file:
            data = json.load(file)
            data.append(appendData)
        
        #with open(fullname, "w") as file:
            json.dump(data, file)
