import module11
import common_funcs
import packing_classes

if __name__ == '__main__':
    option = None
    while option not in {1, 2, 3}:
        option = int(input("Select Option Number [1-Park, 2-Pickup, 3-History]:"))
    
    packing = packing_classes.Packing()
    if option == 1:
        packing.pack()
    elif option == 2:
        packing.pickup()
    else:
        packing.history()
