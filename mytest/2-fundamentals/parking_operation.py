import parking_info

class ParkingOperation:
  

    def park():
        parkingInfo = parking_info.ParkingInfo("", {}, None)
        parkingInfo.inputPackingInfo()
        parkingInfo.saveParkingInfo()
        print("Parking Completed. Welcome!")


    def pickup():
        parkingInfo= parking_info.ParkingInfo.inputPickUpCar()
        parkingInfo.calculateFeeAndSave()
        print("PickUp Completed. Thank you for payment!")
            
            
    def history():
        parkingInfo= parking_info.ParkingInfo.inputCarIndentity()
        parkingInfo.ExportPackingHistory()
        print("Packing History exported. Please check file [" + parkingInfo.PARKING_HISTORY_FOLDER + parkingInfo.car_identity + ".txt]")
       