import parking_operation

#---------------------------------
# CONSOLE APP: CAR PARKING SYSTEM
#---------------------------------

if __name__ == '__main__':
    option = None
    while True:
        option = int(input("Select Option Number [1-Park, 2-Pickup, 3-History]:"))
        if option == 1:
            parking_operation.ParkingOperation.park()
        elif option == 2:
            parking_operation.ParkingOperation.pickup()
            break
        elif option == 3:
            parking_operation.ParkingOperation.history()
            break
        else:
            continue
            
