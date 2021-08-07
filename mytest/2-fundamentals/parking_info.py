import datetime
import re
import string
import json
import os

class ParkingInfo:
    DATETIME_FORMAT = '%Y-%m-%d %H:%M'
    PARKING_DATA_FOLDER = "./parking-data/parking/" 
    
    ##
    car_identity = ""
    arrival_time = ""
    frequency_number = ""

    def __init__(self):
        pass
  
    def getCurrentTime():
        return datetime.datetime.now().strftime(ParkingInfo.DATETIME_FORMAT)

    def isValidParkTime( strtime):
        isValid = True
        try:
            datetime.datetime.strptime(strtime, ParkingInfo.DATETIME_FORMAT)
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
        fullname = ParkingInfo.PARKING_DATA_FOLDER + self.car_identity + ".json"

        # First time parking for this car, init data-json file for this car
        jsonInit = {"available-credit" : 0, "parking-infos" : []}
        if not os.path.isfile(fullname):
            with open(fullname,"w") as file:
                json.dump(jsonInit, file)
        
        # Parking infor for this packing
        parkInfo = {
            "parking-time": self.arrival_time,
            "frequency-number": self.frequency_number,
            "pickup-time" : "",
            "payment-amount" : 0
        }
    
        parkInfos = None
        # Append this parking to the file for this car
        with open(fullname , "r") as file:
            parkInfos = json.load(file)
            parkInfos["parking-infos"].append(parkInfo)

        # Save file
        with open(fullname, "w") as file:
            json.dump(parkInfos, file)

    def findPackingInfo(carIdentity):
        carIdentity = string.strip(carIdentity)
        if not ParkingInfo.isValidCarIdentity(carIdentity):
            raise NameError('Invalid Car Identity')
        else:
            found = False
            fullname = ParkingInfo.PARKING_DATA_FOLDER + carIdentity + ".json"
            if not os.path.isfile(fullname):
                raise NameError("This car ever parked yet")
            else:
                with open(fullname , "r") as file:
                    parkInfos = json.load(file)
                    packing = list(filter(lambda x: (x["pickup-time"] == ""), parkInfos["parking-infos"]))
                    if len(packing) != 1:
                        raise NameError("This car already picked up")
                    else:
                        return parkInfos


    def inputPickUpCar() :        
        car_identity = str(input('Car Identity (ex: 01A-12345):'))
        car_identity = string.strip(car_identity)

        if not ParkingInfo.isValidCarIdentity(car_identity):
            raise NameError('Invalid Car Identity')
        
        fullname = ParkingInfo.PARKING_DATA_FOLDER + car_identity + ".json"
        if not os.path.isfile(fullname):
            raise NameError("This car ever parked yet")
        
        activeParkingInfo = None
        parkInfos = None
        with open(fullname , "r") as file:
            parkInfos = json.load(file)
            activeParkingInfo = list(filter(lambda x: (x["pickup-time"] == ""), parkInfos["parking-infos"]))
            if len(activeParkingInfo) != 1:
                raise NameError("This car already picked up")
        
        

      

        
        
       
# guru99.com/reading-and-writing-files-in-python.html