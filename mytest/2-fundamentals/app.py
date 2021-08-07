import packing_operation

if __name__ == '__main__':
    option = None
    while option not in {1, 2, 3}:
        option = int(input("Select Option Number [1-Park, 2-Pickup, 3-History]:"))
    
    
    if option == 1:
        packing_operation.ParkingOperation.park()
    elif option == 2:
        packing_operation.ParkingOperation.pickup()
    else:
        packing_operation.ParkingOperation.history()
