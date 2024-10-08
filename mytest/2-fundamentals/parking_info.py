import datetime
import re
import string
import json
import os
import parking_fee

class ParkingInfo:
    """
    The Class to encapsulate the parking information
    """
    DATETIME_FORMAT = '%Y-%m-%d %H:%M'
    PARKING_DATA_FOLDER = "./parking-data/parking/" 
    PARKING_HISTORY_FOLDER = "./parking-data/parking-history/" 
    
    ##
    car_identity = ""
    arrival_time = ""
    frequency_number = ""

    #
    parkInfos = []
    activeParkingInfo = None

    def __init__(self,  car_identity, parkInfos, activeParkingInfo):
        self.car_identity = car_identity
        self.parkInfos = parkInfos
        self.activeParkingInfo = activeParkingInfo
  
    def getCurrentTime():
        return datetime.datetime.now().strftime(ParkingInfo.DATETIME_FORMAT)

    def isValidParkTime( strtime):
        """
        Verify the time string input is valid with required formation of this app
        Input
           strtime: the time text
        Return
           True of False
        """
        isValid = True
        try:
            datetime.datetime.strptime(strtime, ParkingInfo.DATETIME_FORMAT)
        except Exception:
            isValid = False
        return 
        
    def isValidCarIdentity(id):
        """
        Verify the car id input is valid with required formation of this app
        Input
           id: the car id
        Return
           True of False
        """
        p = re.compile("^[0-9]{2}[A-Z]{1}[-]{1}[0-9]{5}$")
        return p.match(id)
    
    def isValidFrequencyNumber(digits):
        """
        Verify the frequency numer input is valid with required formation of this app
        Input
           digits: the number
        Return
           True of False
        """
        digits = digits.strip()
        if digits.isdigit() and (len(digits) == 5):
            origin = digits[: 4]
            addsum = sum((len(origin) + 1 - pos)*int(num) for pos,num in enumerate(origin))
            check_digit = 11 - (addsum % 11)
            return int(digits[4:]) == check_digit
        else:
            return False

    def inputPackingInfo(self) :
        """
        Capture user parking input and validate it
        Input
           This object
        """
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
        while True:
        # Car IdentitY
            self.car_identity = str(input('Car Identity (ex: 01A-12345):'))
            if ParkingInfo.isValidCarIdentity(self.car_identity):
                break
            else:
                print('Invalid identiy, re-enter gain')
        while True:
        # Frequency Number
            self.frequency_number = str(input('Frequency Number (ex: 12343):'))
            if ParkingInfo.isValidFrequencyNumber(self.frequency_number):
                break
            else:
                print('Invalid frequencey number, re-enter gain')
    
    def saveParkingInfo(self):
        """
        Save the parking informatin to json file to be used later at pickup or history
        One car id is one json file
        Input
           This object
        """
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

    def inputPickUpCar() :
        """
        Capture user picking input and validate it
        Input
           This object
        """        
        car_identity = str(input('Car Identity (ex: 01A-12345):'))
        car_identity = car_identity.strip()

        if not ParkingInfo.isValidCarIdentity(car_identity):
            raise NameError('Invalid Car Identity')
        
        fullname = ParkingInfo.PARKING_DATA_FOLDER + car_identity + ".json"
        if not os.path.isfile(fullname):
            raise NameError("This car ever parked yet")
        
        activeParkingInfos = None
        parkInfos = None
        with open(fullname , "r") as file:
            parkInfos = json.load(file)
            activeParkingInfos = list(filter(lambda x: (x["pickup-time"] == ""), parkInfos["parking-infos"]))
            if len(activeParkingInfos) != 1:
                raise NameError("This car already picked up")
        
        parkingInfo = ParkingInfo(car_identity, parkInfos, activeParkingInfos[0])
        return parkingInfo
    
    def calculateFeeAndSave(self) : 
        """
        Calculate parking free for the car provided and save to json file for use later
        One car id is one json file
        Input
           This object
        """
        pickTimeStr = ParkingInfo.getCurrentTime()
        fee = parking_fee.calculateParkingFee(self.activeParkingInfo["parking-time"],
                                        pickTimeStr, ParkingInfo.DATETIME_FORMAT)
        payment = 0
        exceedAmount = 0
        avaiableCredit = self.parkInfos["available-credit"]
        print("Fee = " + "{:.2f}".format(fee) + " [Available credit = " +  "{:.2f}".format(avaiableCredit) + "]")
        while True:
            payment = float(input("Enter the payment: "))
            exceedAmount = payment + avaiableCredit - fee
            if exceedAmount >= 0:
                break
            else:
                print("Not enough payment, enter again")
        
        # Payment done, update payment for this parking
        self.activeParkingInfo["pickup-time"] = pickTimeStr
        self.activeParkingInfo["payment-amount"] = fee
        self.parkInfos["available-credit"] = exceedAmount

        # Save
        fullname = ParkingInfo.PARKING_DATA_FOLDER + self.car_identity + ".json"
        with open(fullname, "w") as file:
            json.dump(self.parkInfos, file)

    def inputCarIndentity() : 
        """
        Capture car id and validate it
        """       
        car_identity = str(input('Car Identity (ex: 01A-12345):'))
        car_identity = car_identity.strip()

        if not ParkingInfo.isValidCarIdentity(car_identity):
            raise NameError('Invalid Car Identity')
        
        fullname = ParkingInfo.PARKING_DATA_FOLDER + car_identity + ".json"
        if not os.path.isfile(fullname):
            raise NameError("This car ever parked yet")

        parkInfos = None
        with open(fullname , "r") as file:
            parkInfos = json.load(file)
            
        parkingInfo = ParkingInfo(car_identity, parkInfos, None)
        return parkingInfo  
       
    def ExportPackingHistory(self):
        """
        Export parking history of this car to txt file based on the data in json file
        """ 
        fullname = ParkingInfo.PARKING_HISTORY_FOLDER + self.car_identity + ".txt"
        f= open(fullname,"w")

        availbleCredit = self.parkInfos["available-credit"]
        totalPayment  = availbleCredit
        for pk in range(len(self.parkInfos["parking-infos"])):
            totalPayment = totalPayment + self.parkInfos["parking-infos"][pk]["payment-amount"]
    
        f.write("Total payment: "+ "{:.2f}".format(totalPayment)+"\n")
        f.write("Available credits: "+ "{:.2f}".format(availbleCredit)+"\n")
        f.write("Parked Dates:" +"\n")

        for pk in range(len(self.parkInfos["parking-infos"])):
            strParkTime = self.parkInfos["parking-infos"][pk]["parking-time"]
            strPickTime = self.parkInfos["parking-infos"][pk]["pickup-time"]
            parkTime = datetime.datetime.strptime(strParkTime, ParkingInfo.DATETIME_FORMAT)
            pickTime = parkTime
            if len(strPickTime) > 0:
                pickTime = datetime.datetime.strptime(strPickTime, ParkingInfo.DATETIME_FORMAT)
    
            totalDurationInMinutes = (pickTime - parkTime).total_seconds() // 60
            totalDurationInHour = int(totalDurationInMinutes//60)
            remainMinutes = int(totalDurationInMinutes % 60)
            strDuration = str(totalDurationInHour) + ":" + str(remainMinutes)
            if len(strPickTime) == 0:
                strDuration = "N/A"

            f.write(strParkTime + " - " + strDuration + "\n")
                    
        f.close() 