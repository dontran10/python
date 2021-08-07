import parking_info


class ParkingOperation:
  

    def park():
        parkingInfo = parking_info.ParkingInfo()
        #car.inputPackingInfo()
        parkingInfo.car_identity = "01A-12345"
        parkingInfo.saveParkingInfo()


    def pickup():
        parkingInfo = parking_info.ParkingInfo.inputPickUpCar()

            
            
    def history():
        print('history')